import sys
import unittest
from pathlib import Path
from types import SimpleNamespace


RAG_DIR = Path(__file__).resolve().parents[1] / "rag"
sys.path.insert(0, str(RAG_DIR))

from answer_vllm import placeholder_clarification, resolve_method  # noqa: E402
from prompts import build_prompt  # noqa: E402


def method_args(method: str, **overrides):
    values = {
        "method": method,
        "route_boost_weight": 1.0,
        "confidence_threshold": None,
        "semantic_threshold": None,
    }
    values.update(overrides)
    return SimpleNamespace(**values)


class ExperimentMethodTests(unittest.TestCase):
    def test_m0_disables_retrieval(self):
        config = resolve_method(method_args("m0_llm_only"))
        self.assertFalse(config["use_retrieval"])
        self.assertEqual(config["prompt_mode"], "llm_only")

    def test_m1_is_pure_semantic_retrieval(self):
        config = resolve_method(method_args("m1_rag_simple"))
        self.assertEqual(config["retrieval_mode"], "semantic")
        self.assertEqual(config["route_boost_weight"], 0.0)

    def test_m2_uses_requested_heuristic_weight(self):
        config = resolve_method(
            method_args("m2_rag_rerank", route_boost_weight=0.75)
        )
        self.assertEqual(config["retrieval_mode"], "heuristic_rerank")
        self.assertEqual(config["route_boost_weight"], 0.75)

    def test_m3_requires_a_calibrated_threshold(self):
        with self.assertRaises(RuntimeError):
            resolve_method(method_args("m3_rag_threshold"))

        config = resolve_method(
            method_args("m3_rag_threshold", semantic_threshold=0.82)
        )
        self.assertTrue(config["use_threshold"])
        self.assertEqual(config["route_boost_weight"], 1.0)
        self.assertEqual(config["prompt_mode"], "standard")

    def test_m4_uses_strict_prompt_with_threshold(self):
        with self.assertRaises(RuntimeError):
            resolve_method(method_args("m4_rag_abstention"))
        config = resolve_method(
            method_args("m4_rag_abstention", semantic_threshold=0.85)
        )
        self.assertEqual(config["prompt_mode"], "strict_abstention")
        self.assertTrue(config["use_threshold"])
        self.assertEqual(config["route_boost_weight"], 1.0)

    def test_placeholder_clarification_is_deterministic(self):
        message = placeholder_clarification(
            "Comment contacter le secrétariat de la composante XXX ?"
        )
        self.assertIn("préciser", message)
        self.assertIsNone(placeholder_clarification("Comment candidater en master ?"))

    def test_application_dates_without_level_require_clarification(self):
        message = placeholder_clarification(
            "Quelles sont les dates de candidature pour l'année universitaire en cours ?"
        )
        self.assertIn("niveau d'entrée", message)

    def test_application_dates_with_level_do_not_force_clarification(self):
        self.assertIsNone(
            placeholder_clarification("Quelles sont les dates de candidature en M1 ?")
        )

    def test_french_level_without_program_requires_clarification(self):
        message = placeholder_clarification(
            "Quel niveau de français est nécessaire pour suivre une formation à l'Inalco ?"
        )
        self.assertIn("niveau de français", message)

    def test_french_level_for_exchange_student_is_specific(self):
        self.assertIsNone(
            placeholder_clarification(
                "Quel niveau de français faut-il pour un étudiant en échange ?"
            )
        )

    def test_llm_only_prompt_has_no_fake_context_or_sources(self):
        prompt = build_prompt("Quelle est l'adresse ?", [], mode="llm_only")
        self.assertEqual(prompt.context, "")
        self.assertEqual(prompt.source_urls, [])
        self.assertEqual(prompt.context_hit_ranks, [])
        self.assertNotIn("CONTEXTE", prompt.user_prompt)

    def test_prompt_tracks_only_hits_included_in_context(self):
        hits = [
            {
                "text": "A" * 20,
                "metadata": {"source_url": "https://example.test/one"},
            },
            {
                "text": "B" * 20,
                "metadata": {"source_url": "https://example.test/two"},
            },
        ]
        prompt = build_prompt(
            "Question ?",
            hits,
            max_context_chars=500,
            max_chunk_chars=20,
            include_scores=False,
        )
        self.assertEqual(prompt.context_hit_ranks, [1])
        self.assertEqual(prompt.source_urls, ["https://example.test/one"])

    def test_placeholder_instruction_precedes_abstention(self):
        prompt = build_prompt("Composante XXX ?", [], mode="standard")
        clarification = prompt.user_prompt.index("question de clarification")
        abstention = prompt.user_prompt.index("contexte est insuffisant")
        self.assertLess(clarification, abstention)

    def test_prompt_forbids_reconstructing_incomplete_lists(self):
        prompt = build_prompt("Quelles langues sont enseignées ?", [], mode="standard")
        self.assertIn("ne tente pas de la reconstituer", prompt.user_prompt)
        self.assertIn("catalogue officiel des langues", prompt.user_prompt)
        self.assertIn("niveaux de français", prompt.user_prompt)

    def test_prompt_removes_invalid_placeholder_links(self):
        hits = [
            {
                "text": "Contactez le service : [Voir l'e-mail](#).",
                "metadata": {"source_url": "https://example.test/contact"},
            }
        ]
        prompt = build_prompt("Comment contacter le service ?", hits)
        self.assertNotIn("[Voir l'e-mail](#)", prompt.context)


if __name__ == "__main__":
    unittest.main()
