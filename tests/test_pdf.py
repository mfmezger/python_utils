"""Tests for document to PDF conversion."""

from pathlib import Path
from unittest.mock import patch

import pytest

from python_utils.pdf.convert_docs_to_pdf import convert_docs_to_pdf


class TestConvertDocsToPdf:
    """Tests for convert_docs_to_pdf function."""

    def test_directory_not_found(
        self, tmp_path: Path, caplog: pytest.LogCaptureFixture
    ) -> None:
        """Test error when directory doesn't exist."""
        with patch("python_utils.pdf.convert_docs_to_pdf.logger") as mock_logger:
            convert_docs_to_pdf(tmp_path / "nonexistent")
            mock_logger.error.assert_called_once()

    def test_empty_directory(self, tmp_path: Path) -> None:
        """Test handling of directory with no doc files."""
        # Should complete without error
        convert_docs_to_pdf(tmp_path)
