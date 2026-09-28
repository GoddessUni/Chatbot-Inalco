import sys
import unittest
from pathlib import Path


SCRAPER_DIR = Path(__file__).resolve().parents[1] / "scraper"
sys.path.insert(0, str(SCRAPER_DIR))

from config import (  # noqa: E402
    INALCO_ALLOWED_PATHS,
    INALCO_TEMPORAL_EXACT_PATHS,
    SEED_URLS,
)
from crawler import is_allowed_url  # noqa: E402
from page_filter import classify_page  # noqa: E402


class InstitutionalWhitelistTests(unittest.TestCase):
    def test_official_language_catalogue_is_allowed(self):
        path = "/les-langues-et-civilisations-enseignees-linalco"
        self.assertIn(path, INALCO_ALLOWED_PATHS)
        self.assertIn(f"https://www.inalco.fr{path}", SEED_URLS)

    def test_ajac_source_is_allowed_and_temporal(self):
        path = "/inscriptions-administratives"
        url = f"https://www.inalco.fr{path}"
        self.assertIn(path, INALCO_ALLOWED_PATHS)
        self.assertIn(path, INALCO_TEMPORAL_EXACT_PATHS)
        self.assertTrue(is_allowed_url(url))
        self.assertEqual(
            classify_page({"source_url": url})["knowledge_type"],
            "temporal",
        )

    def test_student_regulations_are_allowed_and_temporal(self):
        path = "/reglements-et-chartes-etudiantes"
        url = f"https://www.inalco.fr{path}"
        self.assertIn(path, INALCO_ALLOWED_PATHS)
        self.assertIn(path, INALCO_TEMPORAL_EXACT_PATHS)
        self.assertTrue(is_allowed_url(url))
        self.assertEqual(
            classify_page({"source_url": url})["knowledge_type"],
            "temporal",
        )


if __name__ == "__main__":
    unittest.main()
