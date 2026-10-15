"""Regression checks for fixture boundaries, not a semantic verifier."""

import contextlib
import copy
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from jsonschema import Draft202012Validator, FormatChecker

import validate_safe_galc_vectors as harness


class CandidateContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = harness._load_json(harness.SCHEMA_PATH)
        cls.vectors = harness._load_json(harness.VECTORS_PATH)
        cls.validator = Draft202012Validator(cls.schema, format_checker=FormatChecker())

    def case(self, number):
        vector = copy.deepcopy(self.vectors["vectors"][number - 1])
        materialized = harness._materialize_vector(self.vectors, vector)
        return {
            "vector": vector,
            "fixture_envelope": materialized["base_lifecycle"],
            "scenario_input": harness._project_scenario_input(
                materialized["base_lifecycle"]
            ),
            "verification_context": materialized["base_verification_context"],
        }

    def run_cli(self, *arguments):
        output = io.StringIO()
        with patch("sys.argv", ["validate_safe_galc_vectors.py", *arguments]):
            with contextlib.redirect_stdout(output):
                code = harness.main()
        return code, output.getvalue()

    def test_inventory_and_structural_outcomes(self):
        self.assertEqual(len(self.vectors["vectors"]), 22)
        self.assertTrue(self.validator.is_valid(self.vectors["base_lifecycle"]))
        for number in range(1, 23):
            with self.subTest(number=number):
                case = self.case(number)
                harness._validate_vector_scope(case["vector"], self.schema)
                self.assertEqual(
                    self.validator.is_valid(case["fixture_envelope"]),
                    number not in {17, 18, 19},
                )

    def test_output_negative_retains_invalid_fixture_but_has_no_semantic_oracle(self):
        baseline, negative = self.case(1), self.case(18)
        self.assertEqual(baseline["scenario_input"], negative["scenario_input"])
        self.assertEqual(
            baseline["verification_context"], negative["verification_context"]
        )
        self.assertNotEqual(baseline["fixture_envelope"], negative["fixture_envelope"])
        harness._check_oracle_consistency([baseline, negative])
        for number in (17, 18, 19):
            artifact = harness._expected_output(self.case(number)["vector"])
            self.assertNotIn("semantic_verifier_output", artifact)
            self.assertEqual(
                artifact["semantic_comparison"]["status"], "not_applicable"
            )

    def test_structural_negative_rejects_semantic_oracle(self):
        for number in (17, 18, 19):
            vector = self.case(number)["vector"]
            vector["expected"]["overall_result"] = "correlation_failed"
            with self.subTest(number=number), self.assertRaisesRegex(
                ValueError, "no semantic oracle"
            ):
                harness._validate_vector_scope(vector, self.schema)

    def test_identical_inputs_reject_conflicting_aggregate(self):
        first = self.case(1)
        second = copy.deepcopy(first)
        second["vector"]["id"] = "TEST-conflict"
        second["vector"]["expected"]["overall_result"] = "correlation_failed"
        with self.assertRaisesRegex(ValueError, "incompatible semantic oracles"):
            harness._check_oracle_consistency([first, second])

    def test_identical_inputs_reject_conflicting_partial_property(self):
        first = self.case(1)
        second = copy.deepcopy(first)
        second["vector"]["expected"] = {"evaluations": {"execution_binding": "fail"}}
        with self.assertRaisesRegex(ValueError, "property:execution_binding"):
            harness._check_oracle_consistency([first, second])

    def test_compatible_partial_maps_and_key_order(self):
        first = self.case(1)
        second = copy.deepcopy(first)
        second["scenario_input"] = dict(
            reversed(list(second["scenario_input"].items()))
        )
        second["vector"]["expected"] = {"evaluations": {"execution_binding": "pass"}}
        harness._check_oracle_consistency([first, second])
        second["vector"]["expected"]["evaluations"]["execution_binding"] = "fail"
        with self.assertRaises(ValueError):
            harness._check_oracle_consistency([first, second])

    def test_distinct_anchoring_contexts_not_identical_input_conflicts(self):
        cases = [self.case(number) for number in (1, 20, 21, 22)]
        self.assertTrue(
            all(case["scenario_input"] == cases[0]["scenario_input"] for case in cases)
        )
        contexts = {
            json.dumps(case["verification_context"], sort_keys=True) for case in cases
        }
        self.assertEqual(len(contexts), 4)
        harness._check_oracle_consistency(cases)

    def test_expected_values_do_not_materialize_into_inputs(self):
        vector = copy.deepcopy(self.vectors["vectors"][0])
        before = harness._materialize_vector(self.vectors, vector)
        vector["expected"] = {"overall_result": "correlation_failed"}
        self.assertEqual(before, harness._materialize_vector(self.vectors, vector))

    def test_anchored_claim_requires_both_references_on_first_and_last_record(self):
        for position in (0, -1):
            for field in ("reference", "result_ref"):
                lifecycle = copy.deepcopy(self.vectors["base_lifecycle"])
                del lifecycle["records"][position]["anchor"][field]
                with self.subTest(position=position, field=field):
                    self.assertFalse(self.validator.is_valid(lifecycle))
        for state in ("unanchored", "unavailable"):
            lifecycle = copy.deepcopy(self.vectors["base_lifecycle"])
            lifecycle["records"][0]["anchor"] = {"status": state}
            self.assertTrue(self.validator.is_valid(lifecycle))

    def test_cli_emits_separated_artifacts_without_output_leakage(self):
        with tempfile.TemporaryDirectory() as directory:
            code, output = self.run_cli("--emit-dir", directory)
            self.assertEqual(code, 0, output)
            root = Path(directory)
            self.assertEqual(len(list(root.glob("*.json"))), 88)
            for number in range(1, 23):
                prefix = f"GALC-{number:03d}"
                scenario = harness._load_json(root / f"{prefix}.scenario-input.json")
                self.assertTrue(
                    set(harness.VERIFIER_OUTPUT_FIELDS).isdisjoint(scenario)
                )
                fixture = harness._load_json(root / f"{prefix}.fixture-envelope.json")
                self.assertEqual(fixture["artifact_role"], "structural_fixture_only")
                expected = harness._load_json(root / f"{prefix}.expected-output.json")
                self.assertEqual(
                    "semantic_verifier_output" in expected, number not in {17, 18, 19}
                )
            before = {path.name: path.read_bytes() for path in root.iterdir()}
            code, output = self.run_cli("--emit-dir", directory)
            self.assertEqual(code, 1)
            self.assertIn("refusing stale artifacts", output)
            self.assertEqual(
                before, {path.name: path.read_bytes() for path in root.iterdir()}
            )

    def test_cli_blocks_incompatible_oracles_before_emission(self):
        vectors = copy.deepcopy(self.vectors)
        vectors["vectors"][1] = copy.deepcopy(vectors["vectors"][0])
        vectors["vectors"][1]["id"] = "GALC-002"
        vectors["vectors"][1]["expected"]["overall_result"] = "correlation_failed"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "vectors.json"
            source.write_text(json.dumps(vectors), encoding="utf-8")
            destination = root / "emitted"
            with patch.object(harness, "VECTORS_PATH", source):
                code, output = self.run_cli("--emit-dir", str(destination))
            self.assertEqual(code, 1)
            self.assertIn("incompatible semantic oracles", output)
            self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
