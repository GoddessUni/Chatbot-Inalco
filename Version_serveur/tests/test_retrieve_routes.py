import sys
import unittest
from pathlib import Path


RAG_DIR = Path(__file__).resolve().parents[1] / "rag"
sys.path.insert(0, str(RAG_DIR))

from retrieve import (  # noqa: E402
    access_rerank_bonus,
    asks_language_catalogue,
    detect_routes,
    directionally_compatible,
    mobility_direction,
    rerank_bonus,
    select_intent_candidates,
)


class RouteDetectionTests(unittest.TestCase):
    def test_restaurant_attributes_do_not_trigger_building_access(self):
        routes = detect_routes(
            "Quels sont les restaurants et cafétérias près de l'Inalco, "
            "avec leurs adresses et horaires ?"
        )
        self.assertIn("restauration", routes)
        self.assertNotIn("access", routes)

    def test_general_inalco_address_uses_access_route(self):
        self.assertEqual(
            detect_routes("Quelle est l'adresse de l'Inalco ?"),
            ["access"],
        )

    def test_transport_question_uses_access_route(self):
        self.assertEqual(
            detect_routes("Comment se rendre sur les sites de l'Inalco en métro ?"),
            ["access"],
        )

    def test_campus_object_location_keeps_topical_route(self):
        routes = detect_routes("Où se trouve la boîte à don de livres ?")
        self.assertIn("campus_environment", routes)
        self.assertNotIn("access", routes)

    def test_access_reranker_is_disabled_for_multi_topic_query(self):
        record = {
            "metadata": {
                "source_url": "https://www.inalco.fr/la-maison-de-la-recherche",
                "title": "La Maison de la recherche",
                "section_title": "Accès",
            },
            "text": "Adresse, métro, bus et horaires d'ouverture.",
        }
        self.assertEqual(
            rerank_bonus(record, "Comment aller au restaurant ?", ["restauration", "access"]),
            0.0,
        )

    def test_access_reranker_is_capped(self):
        record = {
            "metadata": {
                "source_url": "https://www.inalco.fr/la-maison-de-la-recherche",
                "title": "La Maison de la recherche",
                "section_title": "Accès",
            },
            "text": "Adresse, métro, bus, RER et horaires d'ouverture.",
        }
        self.assertEqual(
            access_rerank_bonus(record, "Comment se rendre à cette adresse en métro ?"),
            0.45,
        )

    def test_incoming_exchange_question_excludes_outgoing_page(self):
        question = "Comment venir étudier à l’Inalco dans le cadre d’un programme d’échange ?"
        outgoing = {
            "metadata": {
                "source_url": (
                    "https://portail-etudiant.inalco.fr/fr/international/"
                    "etudier-a-l-etranger/mobilites-erasmus.html"
                )
            }
        }
        incoming = {
            "metadata": {
                "source_url": (
                    "https://portail-etudiant.inalco.fr/fr/international/"
                    "venir-etudier-a-l-inalco.html"
                )
            }
        }
        self.assertEqual(mobility_direction(question), "incoming")
        self.assertFalse(directionally_compatible(outgoing, question))
        self.assertTrue(directionally_compatible(incoming, question))

    def test_outgoing_exchange_question_excludes_incoming_page(self):
        question = "Comment partir en mobilité pour étudier à l'étranger ?"
        incoming = {
            "metadata": {
                "source_url": (
                    "https://portail-etudiant.inalco.fr/fr/international/"
                    "venir-etudier-a-l-inalco.html"
                )
            }
        }
        self.assertEqual(mobility_direction(question), "outgoing")
        self.assertFalse(directionally_compatible(incoming, question))

    def test_incoming_question_prefers_incoming_page_when_available(self):
        question = "Comment venir étudier à l'Inalco dans un programme d'échange ?"
        records = [
            {
                "metadata": {
                    "source_url": "https://example.test/international-buddies"
                }
            },
            {
                "metadata": {
                    "source_url": (
                        "https://portail-etudiant.inalco.fr/fr/international/"
                        "venir-etudier-a-l-inalco.html"
                    )
                }
            },
        ]
        selected = select_intent_candidates(records, question)
        self.assertEqual(len(selected), 1)
        self.assertIn("venir-etudier-a-l-inalco", selected[0]["metadata"]["source_url"])

    def test_language_catalogue_question_prefers_official_directory(self):
        question = "Quelles langues peut-on étudier à l'Inalco ?"
        records = [
            {
                "metadata": {
                    "source_url": (
                        "https://portail-etudiant.inalco.fr/fr/international/"
                        "venir-etudier-a-l-inalco.html"
                    )
                }
            },
            {
                "metadata": {
                    "source_url": (
                        "https://www.inalco.fr/"
                        "les-langues-et-civilisations-enseignees-linalco"
                    )
                }
            },
        ]
        self.assertTrue(asks_language_catalogue(question))
        selected = select_intent_candidates(records, question)
        self.assertEqual(len(selected), 1)
        self.assertIn("les-langues-et-civilisations", selected[0]["metadata"]["source_url"])


if __name__ == "__main__":
    unittest.main()
