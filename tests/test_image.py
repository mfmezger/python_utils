"""Tests for PDF to image conversion."""

from pathlib import Path

import pytest

from python_utils.image.convert_pdf_image import convert_pdfs


class TestConvertPdfs:
    """Tests for convert_pdfs function."""

    def test_source_not_exists(self, tmp_path: Path) -> None:
        """Test error when source directory doesn't exist."""
        with pytest.raises(FileNotFoundError, match="Source root does not exist"):
            convert_pdfs(tmp_path / "nonexistent", tmp_path / "output")

    def test_creates_dest_directory(self, tmp_path: Path) -> None:
        """Test that destination directory is created if it doesn't exist."""
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "output" / "nested"

        # No PDFs, but should still create dest
        result = convert_pdfs(src, dest)
        assert dest.exists()
        assert result == 0

    def test_empty_directory(self, tmp_path: Path) -> None:
        """Test converting empty directory returns 0."""
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "output"

        result = convert_pdfs(src, dest)
        assert result == 0
