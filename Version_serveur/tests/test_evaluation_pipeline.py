import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EVALUATION_DIR = PROJECT_ROOT / "evaluation"
sys.path.insert(0, str(EVALUATION_DIR))

from calibrate_threshold import metrics_for  # noqa: E402
from evaluate_retrieval_gold import evidence_matches_hit  # noqa: E402
from score_behavior import actual_behavior  # noqa: E402


class EvaluationPipelineTests(unittest.TestCase):
    def test_gold_evidence_requires_the_correct_section_on_shared_page(self):
        evidence = {
            "source_url": "https://example.test/page?query=ignored",
            "section_title": "Cafétéria des Grands Moulins",
            "page_start": None,
        }
        wrong = {
            "metadata": {
                "source_url": "https://example.test/page",
                "section_title": "Cafétéria de l'Inalco",
            }
        }
        correct = {
            "metadata": {
                "source_url": "https://example.test/page",
                "section_title": "Cafétéria des Grands Moulins",
            }
        }
        self.assertFalse(evidence_matches_hit(evidence, wrong))
        self.assertTrue(evidence_matches_hit(evidence, correct))

    def test_threshold_metrics_count_unsafe_answers(self):
        rows = [
            {"context_has_gold_evidence": True, "top_semantic_score": 0.90},
            {"context_has_gold_evidence": False, "top_semantic_score": 0.85},
        ]
        permissive = metrics_for(rows, 0.80)
        safe = metrics_for(rows, 0.86)
        self.assertEqual(permissive["fp"], 1)
        self.assertEqual(safe["fp"], 0)
        self.assertEqual(safe["tp"], 1)

    def test_legacy_clarification_can_be_scored(self):
        row = {
            "answer": "Veuillez préciser la composante qui vous intéresse.",
            "abstain": False,
        }
        self.assertEqual(actual_behavior(row), "clarify")


if __name__ == "__main__":
    unittest.main()
