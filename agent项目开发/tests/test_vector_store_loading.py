import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from rag.vector_store import VectorStoreService
from utils.config_handler import chrome_config
from utils.file_handler import get_file_md_hex, listdir_with_allowed_type, pdf_loader


class VectorStoreLoadingTests(unittest.TestCase):
    def test_missing_data_directory_returns_no_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = os.path.join(temp_dir, "missing")
            self.assertEqual(listdir_with_allowed_type(missing, ("txt", "pdf")), [])

    def test_loads_documents_from_project_relative_data_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = Path(temp_dir) / "data"
            data_dir.mkdir()
            (data_dir / "example.txt").write_text("A short document.", encoding="utf-8")
            chroma = Mock()
            settings = {
                "data_path": "data",
                "persist_directory": "chroma_db",
                "md5_hex_store": "md5.txt",
            }
            with (
                patch.dict(chrome_config, settings),
                patch("rag.vector_store.get_abs_path", side_effect=lambda path: os.path.join(temp_dir, path)),
                patch("rag.vector_store.Chroma", return_value=chroma) as chroma_class,
                patch("rag.vector_store.get_file_md_hex", return_value="test-digest"),
            ):
                service = VectorStoreService()
                service.load_document()

            self.assertEqual(
                chroma_class.call_args.kwargs["persist_directory"],
                os.path.join(temp_dir, "chroma_db"),
            )
            chroma.add_documents.assert_called_once()
            self.assertEqual((Path(temp_dir) / "md5.txt").read_text(encoding="utf-8"), "test-digest\n")

    def test_md5_reads_to_end_of_nonempty_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "document.txt"
            contents = b"test" * 1500
            source.write_bytes(contents)
            result = subprocess.run(
                [sys.executable, "-X", "utf8", "-c",
                 "from utils.file_handler import get_file_md_hex; "
                 "import sys; print(get_file_md_hex(sys.argv[1]))", str(source)],
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True,
                timeout=5,
                check=True,
            )
            self.assertEqual(result.stdout.strip(), hashlib.md5(contents).hexdigest())

    def test_pdf_loader_accepts_file_without_password(self):
        with patch("utils.file_handler.PyPDFLoader") as loader:
            pdf_loader("example.pdf")
        loader.assert_called_once_with("example.pdf", None)


if __name__ == "__main__":
    unittest.main()
