"""Python utilities for PDF/image conversion, JSON processing, and AI agents."""

from pathlib import Path

import typer

app = typer.Typer(
    name="python-utils",
    help="A collection of Python utilities for PDF/image conversion, JSON processing, and AI agent initialization.",
    no_args_is_help=True,
)


@app.command()
def json2excel(
    input_path: Path = typer.Argument(..., help="Path to JSON file or directory"),
    output: Path | None = typer.Option(None, "--output", "-o", help="Output path"),
    pattern: str = typer.Option("*.json", "--pattern", "-p", help="Glob pattern"),
) -> None:
    """Convert JSON files to Excel format."""
    from python_utils.json2excel.json_to_excel import (
        convert_directory_to_excel,
        convert_json_to_excel,
    )

    if not input_path.exists():
        typer.echo(f"Error: {input_path} does not exist", err=True)
        raise typer.Exit(1)

    if input_path.is_file():
        output_file = convert_json_to_excel(input_path, output)
        typer.echo(f"Successfully converted to: {output_file}")
    elif input_path.is_dir():
        output_files = convert_directory_to_excel(input_path, output, pattern)
        typer.echo(f"\nSuccessfully converted {len(output_files)} file(s)")


@app.command()
def pdf2image(
    source: Path = typer.Argument(..., help="Source directory containing PDFs"),
    dest: Path = typer.Argument(..., help="Destination directory for images"),
) -> None:
    """Convert PDF files to PNG images (300 DPI)."""
    from python_utils.image.convert_pdf_image import convert_pdfs

    total = convert_pdfs(source, dest)
    typer.echo(f"Done. Images written: {total}")


@app.command()
def doc2pdf(
    directory: Path = typer.Argument(..., help="Directory containing .doc/.docx files"),
) -> None:
    """Convert .doc/.docx files to PDF using LibreOffice."""
    from python_utils.pdf.convert_docs_to_pdf import convert_docs_to_pdf

    convert_docs_to_pdf(directory)


def main() -> None:
    """CLI entrypoint."""
    app()
