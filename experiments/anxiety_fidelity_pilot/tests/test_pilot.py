import json
import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pilot


class TestPilot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = pilot.load_stimuli(pilot.HERE / "stimuli.json")

    def test_disjoint_stimuli(self):
        a = {x["id"] for x in self.data["assessment"]}
        t = {x["id"] for x in self.data["training"]}
        self.assertFalse(a & t)

    def test_condition_counts(self):
        for cond, expected in [("positive", 9), ("balanced", 5)]:
            _, xs = pilot.training_block(self.data["training"], cond, random.Random(6))
            self.assertEqual(sum(x["valence"] == "positive" for x in xs), expected)

    def test_hidden_labels_and_validated_scores(self):
        examples = self.data["assessment"][:6]
        prompt, mapping = pilot.format_assessment(examples, random.Random(5))
        self.assertNotIn("[record rating as", prompt)
        xs = pilot.validate(pilot.mock_response(examples, random.Random(2)), examples, mapping)
        self.assertEqual(len(xs), 6)
        raw = {"ratings": [{"id": x["id"], "x": 9, "y": 2} for x in examples]}
        with self.assertRaises(ValueError):
            pilot.validate(json.dumps(raw), examples, mapping)

    def test_mock_pipeline(self):
        a = pilot.run_one(self.data, "positive", 0, 17, "mock", None, None)
        b = pilot.run_one(self.data, "balanced", 1, 19, "mock", None, None)
        self.assertIsInstance(pilot.summarize([a, b])["difference_in_differences"], float)


if __name__ == "__main__":
    unittest.main()

