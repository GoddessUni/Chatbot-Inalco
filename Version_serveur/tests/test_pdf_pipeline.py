import sys
import unittest
from pathlib import Path


SCRAPER_DIR = Path(__file__).resolve().parents[1] / "scraper"
sys.path.insert(0, str(SCRAPER_DIR))

from chunker import build_chunks  # noqa: E402
from cleaner import clean_page  # noqa: E402
from config import PDF_SOURCES  # noqa: E402
from crawler import is_allowed_url  # noqa: E402
from kb_builder import build_embedding_text  # noqa: E402
from metadata import enrich_chunk  # noqa: E402
from page_filter import classify_page  # noqa: E402
from quality import assess_chunk, build_review_record  # noqa: E402


class PdfPipelineTests(unittest.TestCase):
    def setUp(self):
        self.page = {
            "source_url": "https://www.inalco.fr/sites/default/files/test.pdf",
            "parent_url": "https://www.inalco.fr/ddrse",
            "title": "Schema directeur DD&RSE 2025-2030",
            "document_title": "Schema directeur DD&RSE 2025-2030",
            "html_title": "Schema directeur DD&RSE 2025-2030",
            "language": "fr",
            "content_type": "pdf",
            "source_type": "official_pdf",
            "knowledge_type": "temporal",
            "validity_period": "2025-2030",
            "last_seen": "2026-09-15",
            "file_sha256": "abc123",
            "file_size_bytes": 1234,
            "pdf_pages_total": 2,
            "pdf_pages_extracted": 2,
            "text": "Objectif environnemental avec des actions concretes.",
            "sections": [
                {
                    "section_title": "Page 2 - OBJECTIF",
                    "text": "Objectif environnemental avec des actions concretes.",
                    "page_start": 2,
                    "page_end": 2,
                }
            ],
        }

    def test_controlled_sources_and_landing_pages_are_configured(self):
        self.assertEqual(len(PDF_SOURCES), 2)
        for source in PDF_SOURCES:
            self.assertTrue(source["source_url"].lower().endswith(".pdf"))
            self.assertTrue(is_allowed_url(source["parent_url"]))
            self.assertEqual(source["knowledge_type"], "temporal")

    def test_pdf_metadata_survives_clean_classify_chunk_and_embedding(self):
        page = classify_page(clean_page(self.page))
        chunks = [enrich_chunk(chunk) for chunk in build_chunks(page)]

        self.assertEqual(len(chunks), 1)
        chunk = chunks[0]
        self.assertEqual(chunk["content_type"], "pdf")
        self.assertEqual(chunk["source_type"], "official_pdf")
        self.assertEqual(chunk["page_start"], 2)
        self.assertEqual(chunk["page_end"], 2)
        self.assertEqual(chunk["validity_period"], "2025-2030")
        self.assertEqual(
            chunk["theme"], "Environnement et responsabilité sociale"
        )

        embedding_text = build_embedding_text(chunk)
        self.assertIn("Type de contenu: pdf", embedding_text)
        self.assertIn("Pages: 2", embedding_text)
        self.assertIn("Période de validité: 2025-2030", embedding_text)

        assessed, rejection_reasons, _ = assess_chunk(chunk)
        self.assertFalse(rejection_reasons)
        review = build_review_record(assessed)
        self.assertIsNotNone(review)
        self.assertEqual(review["page_start"], 2)
        self.assertEqual(review["document_title"], chunk["document_title"])


if __name__ == "__main__":
    unittest.main()
