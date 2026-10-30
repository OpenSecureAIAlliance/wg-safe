#!/usr/bin/env python3
"""Structural materializer and validator for SAFE-GALC candidate vectors.

This harness checks JSON Schema Draft 2020-12 structure and reproducible
application of the candidate vector operations and oracle consistency. It emits
labelled fixtures, scenario inputs, contexts, and scoped expectations separately.
It does not compute semantic results, verify cryptography,
recompute payload digests, or establish semantic/runtime conformance.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "safe-galc-v0.1.schema.json"
VECTORS_PATH = ROOT / "safe-galc-v0.1.conformance-vectors.json"
ALLOWED_OPERATIONS = {"add", "remove", "replace"}
VERIFIER_OUTPUT_FIELDS = ("evaluations", "overall_result")
TEST_SCOPES = {
    "semantic_scenario",
    "structural_input_negative",
    "output_envelope_negative",
}
PROPERTY_RESULTS = {"pass", "fail", "insufficient_evidence", "not_applicable"}
OVERALL_RESULTS = {
    "correlated",
    "correlation_failed",
    "insufficient_evidence",
    "not_applicable",
}
COMPARISON_RULE = "safe-galc/0.1/partial-expectations/1"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Materialize and structurally validate SAFE-GALC candidate vectors."
    )
    parser.add_argument(
        "--emit-dir",
        type=Path,
        help=(
            "Write separate labelled fixture-envelope, scenario-input, "
            "verification-context, and expected-output JSON artifacts. "
            "The destination must be empty."
        ),
    )
    return parser.parse_args()


def _pointer_parts(path: str) -> list[str]:
    if not path.startswith("/"):
        raise ValueError(f"JSON Pointer must start with '/': {path!r}")
    return [part.replace("~1", "/").replace("~0", "~") for part in path[1:].split("/")]


def _apply_operation(document: Any, operation: dict[str, Any]) -> None:
    kind = operation["operation"]
    if kind not in ALLOWED_OPERATIONS:
        raise ValueError(f"Unsupported operation: {kind!r}")

    parts = _pointer_parts(operation["path"])
    parent = document
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]

    leaf = parts[-1]
    if isinstance(parent, list):
        if kind == "add":
            if leaf == "-":
                parent.append(copy.deepcopy(operation["value"]))
            else:
                parent.insert(int(leaf), copy.deepcopy(operation["value"]))
        elif kind == "replace":
            parent[int(leaf)] = copy.deepcopy(operation["value"])
        else:
            parent.pop(int(leaf))
        return

    if kind in {"add", "replace"}:
        parent[leaf] = copy.deepcopy(operation["value"])
    else:
        del parent[leaf]


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def _project_scenario_input(fixture_envelope: dict[str, Any]) -> dict[str, Any]:
    """Remove fixture-only verifier outputs from a changed structural envelope."""
    scenario_input = copy.deepcopy(fixture_envelope)
    for field in VERIFIER_OUTPUT_FIELDS:
        if field not in scenario_input:
            raise ValueError(
                f"structural fixture is missing output placeholder {field!r}"
            )
        del scenario_input[field]

    leaked = [field for field in VERIFIER_OUTPUT_FIELDS if field in scenario_input]
    if leaked:
        raise ValueError(f"verifier output fields leaked into scenario input: {leaked}")
    return scenario_input


def _expected_output(vector: dict[str, Any]) -> dict[str, Any]:
    expected = copy.deepcopy(vector["expected"])
    expected_validation = expected.pop("schema_validation", "pass")
    applicable = vector["test_scope"] == "semantic_scenario"
    output = {
        "scenario_id": vector["id"],
        "test_scope": vector["test_scope"],
        "structural_fixture_validation": {
            "target": "fixture_envelope",
            "expected": expected_validation,
        },
        "semantic_comparison": {
            "status": "applicable" if applicable else "not_applicable",
            "rule_id": COMPARISON_RULE,
            "reason": (
                "Compare independently produced results only after structural success."
                if applicable
                else "Structural negative control; no semantic-output oracle."
            ),
        },
        "forbidden_inference": vector["forbidden_inference"],
    }
    if applicable:
        output["semantic_verifier_output"] = expected
    return output


def _validate_vector_scope(vector: dict[str, Any], schema: dict[str, Any]) -> None:
    scope = vector.get("test_scope")
    if scope not in TEST_SCOPES:
        raise ValueError(f"unknown test_scope: {scope!r}")
    if not isinstance(vector.get("recompute_integrity"), bool):
        raise ValueError("recompute_integrity must be boolean")
    expected = vector["expected"]
    if scope != "semantic_scenario":
        if expected != {"schema_validation": "fail"}:
            raise ValueError("structural negatives must have no semantic oracle")
        return
    if expected.get("schema_validation", "pass") != "pass":
        raise ValueError("semantic scenarios require structural success")
    if set(expected) - {
        "schema_validation",
        "overall_result",
        "evaluations",
        "reason_codes",
    }:
        raise ValueError("unknown expected-output fields")
    if (
        "overall_result" in expected
        and expected["overall_result"] not in OVERALL_RESULTS
    ):
        raise ValueError("unknown expected overall result")
    properties = schema["$defs"]["evaluation"]["properties"]["property"]["enum"]
    evaluations = expected.get("evaluations", {})
    if not isinstance(evaluations, dict) or any(
        prop not in properties or result not in PROPERTY_RESULTS
        for prop, result in evaluations.items()
    ):
        raise ValueError("invalid partial evaluation expectation")
    reasons = expected.get("reason_codes", [])
    if not isinstance(reasons, list) or any(
        not isinstance(code, str) or not code for code in reasons
    ):
        raise ValueError("reason_codes must be a list of nonempty strings")


def _materialize_vector(
    vectors: dict[str, Any], vector: dict[str, Any]
) -> dict[str, Any]:
    materialized = {
        "base_lifecycle": copy.deepcopy(vectors["base_lifecycle"]),
        "base_verification_context": copy.deepcopy(
            vectors["base_verification_context"]
        ),
    }
    for operation in vector["semantic_changes"]:
        _apply_operation(materialized, operation)
    return materialized


def _check_oracle_consistency(cases: list[dict[str, Any]]) -> None:
    """Check compatible partial oracles; do not compute verifier outcomes."""
    groups: dict[str, dict[str, Any]] = {}
    for case in cases:
        vector = case["vector"]
        if vector["test_scope"] != "semantic_scenario":
            continue
        key = json.dumps(
            {
                "scenario_input": case["scenario_input"],
                "verification_context": case["verification_context"],
                "recompute_integrity": vector["recompute_integrity"],
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        group = groups.setdefault(key, {"ids": [], "assertions": {}})
        assertions = {
            f"property:{prop}": value
            for prop, value in vector["expected"].get("evaluations", {}).items()
        }
        if "overall_result" in vector["expected"]:
            assertions["overall_result"] = vector["expected"]["overall_result"]
        for name, value in assertions.items():
            previous = group["assertions"].get(name)
            if previous is not None and previous != value:
                raise ValueError(
                    f"incompatible semantic oracles for {group['ids']} and "
                    f"{vector['id']}: {name} is {previous!r} versus {value!r}"
                )
            group["assertions"][name] = value
        group["ids"].append(vector["id"])


def _write_json(path: Path, document: Any) -> None:
    path.write_text(
        json.dumps(document, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    args = _parse_args()
    schema = _load_json(SCHEMA_PATH)
    vectors = _load_json(VECTORS_PATH)

    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    vector_ids = [vector["id"] for vector in vectors["vectors"]]
    expected_ids = [f"GALC-{index:03d}" for index in range(1, 23)]
    if vector_ids != expected_ids:
        print(
            f"FAIL: expected ordered vector IDs {expected_ids}, received {vector_ids}"
        )
        return 1
    if vectors["manifest"].get("scenario_count") != len(expected_ids):
        print("FAIL: manifest scenario_count does not match the inventory")
        return 1

    base_errors = sorted(
        validator.iter_errors(vectors["base_lifecycle"]),
        key=lambda error: list(error.path),
    )
    if base_errors:
        print("FAIL: base_lifecycle does not validate")
        for error in base_errors:
            print(f"  {list(error.path)}: {error.message}")
        return 1

    print("PASS: schema is valid Draft 2020-12")
    print("PASS: base_lifecycle validates")
    print(
        "BOUNDARY: base_lifecycle evaluations and overall_result are structural "
        "fixture placeholders, not verifier results"
    )
    print(
        "BOUNDARY: projected scenario inputs omit verifier outputs; expected "
        "results remain separate test oracles"
    )

    failed = False
    cases = []
    for vector in vectors["vectors"]:
        try:
            _validate_vector_scope(vector, schema)
            materialized = _materialize_vector(vectors, vector)
        except (KeyError, IndexError, TypeError, ValueError) as error:
            print(f"FAIL: {vector['id']} could not be materialized: {error}")
            failed = True
            continue

        errors = sorted(
            validator.iter_errors(materialized["base_lifecycle"]),
            key=lambda error: list(error.path),
        )
        expected_validation = vector["expected"].get("schema_validation", "pass")
        actual_validation = "fail" if errors else "pass"

        try:
            scenario_input = _project_scenario_input(materialized["base_lifecycle"])
        except ValueError as error:
            print(f"FAIL: {vector['id']} scenario-input projection failed: {error}")
            failed = True
            continue

        cases.append(
            {
                "vector": vector,
                "fixture_envelope": materialized["base_lifecycle"],
                "scenario_input": scenario_input,
                "verification_context": materialized["base_verification_context"],
            }
        )

        if actual_validation != expected_validation:
            print(
                f"FAIL: {vector['id']} expected schema {expected_validation}, "
                f"received {actual_validation}"
            )
            for error in errors[:5]:
                print(f"  {list(error.path)}: {error.message}")
            failed = True
        else:
            label = (
                "expected structural rejection" if errors else "structural validation"
            )
            print(
                f"PASS: {vector['id']} {label}; projected scenario input "
                "contains no verifier outputs"
            )

    if failed:
        return 1

    try:
        _check_oracle_consistency(cases)
    except ValueError as error:
        print(f"FAIL: {error}")
        return 1
    print("PASS: eligible semantic oracles are consistent for identical inputs/context")
    print("PASS: 22 ordered vectors materialized with expected structural outcomes")
    if args.emit_dir is not None:
        if args.emit_dir.exists() and (
            not args.emit_dir.is_dir() or any(args.emit_dir.iterdir())
        ):
            print(
                "FAIL: --emit-dir must be an empty directory; refusing stale artifacts"
            )
            return 1
        args.emit_dir.mkdir(parents=True, exist_ok=True)
        for case in cases:
            vector = case["vector"]
            artifacts = {
                "fixture-envelope": {
                    "artifact_role": "structural_fixture_only",
                    "scenario_id": vector["id"],
                    "test_scope": vector["test_scope"],
                    "fixture_envelope": case["fixture_envelope"],
                },
                "scenario-input": case["scenario_input"],
                "verification-context": case["verification_context"],
                "expected-output": _expected_output(vector),
            }
            for suffix, document in artifacts.items():
                _write_json(args.emit_dir / f"{vector['id']}.{suffix}.json", document)
        print(
            "PASS: separate fixtures, inputs, contexts, and scoped expectations "
            f"emitted to {args.emit_dir}"
        )
    print("LIMIT: no cryptographic, semantic, or runtime conformance is claimed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
