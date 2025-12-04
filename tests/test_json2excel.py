"""Tests for JSON to Excel conversion."""

from pathlib import Path

from python_utils.json2excel.json_to_excel import (
    convert_json_to_excel,
    flatten_json_results,
)


class TestFlattenJsonResults:
    """Tests for flatten_json_results function."""

    def test_empty_results(self) -> None:
        """Test handling of empty results array."""
        json_data = {"model": "test", "has_probs": True, "results": []}
        df = flatten_json_results(json_data)
        assert len(df) == 0

    def test_single_result(self) -> None:
        """Test flattening a single result."""
        json_data = {
            "model": "gpt-4",
            "has_probs": True,
            "results": [
                [
                    {
                        "prompt": "test prompt",
                        "malicious": False,
                        "prob": 0.1,
                        "content": "test content",
                    }
                ]
            ],
        }
        df = flatten_json_results(json_data)
        assert len(df) == 1
        assert df.iloc[0]["model"] == "gpt-4"
        assert df.iloc[0]["prompt"] == "test prompt"
        assert df.iloc[0]["malicious"] == False  # noqa: E712

    def test_multiple_results(self) -> None:
        """Test flattening multiple results."""
        json_data = {
            "model": "gpt-4",
            "has_probs": False,
            "results": [
                [
                    {"prompt": "p1", "malicious": False, "prob": 0.1, "content": "c1"},
                    {"prompt": "p2", "malicious": True, "prob": 0.9, "content": "c2"},
                ]
            ],
        }
        df = flatten_json_results(json_data)
        assert len(df) == 2

    def test_missing_keys(self) -> None:
        """Test handling of missing keys in results."""
        json_data = {"model": None, "has_probs": None, "results": [[{"prompt": "p1"}]]}
        df = flatten_json_results(json_data)
        assert len(df) == 1
        assert df.iloc[0]["model"] is None
        assert df.iloc[0]["malicious"] is None


class TestConvertJsonToExcel:
    """Tests for convert_json_to_excel function."""

    def test_output_path_generation(self, tmp_path: Path) -> None:
        """Test that output path is generated correctly when not provided."""
        json_file = tmp_path / "test.json"
        json_file.write_text('{"model": "test", "has_probs": true, "results": []}')

        result = convert_json_to_excel(json_file)
        assert result == tmp_path / "test.xlsx"

    def test_custom_output_path(self, tmp_path: Path) -> None:
        """Test using a custom output path."""
        json_file = tmp_path / "input.json"
        json_file.write_text('{"model": "test", "has_probs": true, "results": []}')
        output_file = tmp_path / "custom_output.xlsx"

        result = convert_json_to_excel(json_file, output_file)
        assert result == output_file
        assert output_file.exists()
