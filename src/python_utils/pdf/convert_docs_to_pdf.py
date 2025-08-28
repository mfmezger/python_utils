from pathlib import Path
from loguru import logger
import subprocess


def convert_docs_to_pdf(root_dir: str | Path) -> None:
    """
    Recursively finds all .doc files in a directory and converts them to PDF
    using LibreOffice.
    """
    root_path = Path(root_dir)
    if not root_path.is_dir():
        logger.error(f"Error: Directory '{root_path}' not found.")
        return

    for doc_path in root_path.rglob("*.doc"):
        logger.info(f"Converting {doc_path} to PDF...")
        try:
            subprocess.run(
                [
                    "libreoffice",
                    "--headless",
                    "--convert-to",
                    "pdf",
                    "--outdir",
                    str(doc_path.parent),
                    str(doc_path),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            logger.success(f"Successfully converted {doc_path}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Error converting {doc_path}: {e.stderr}")
        except FileNotFoundError:
            logger.error(
                "Error: 'libreoffice' command not found."
                " Please ensure LibreOffice is installed and in your PATH."
            )
            return


if __name__ == "__main__":
    data_dir = "data"
    convert_docs_to_pdf(data_dir)
