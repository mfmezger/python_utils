"""Minimal PDF -> image converter using pathlib and PyMuPDF.

Edit SRC_ROOT and DEST_ROOT below, then run the module. This file intentionally contains
only the essentials: pathlib for paths and fitz (PyMuPDF) for rendering.
"""

from pathlib import Path
from tqdm import tqdm
import fitz


def convert_pdfs(src_root: Path, dest_root: Path) -> int:
    """Convert all PDFs under src_root to PNG images under dest_root.

    Preserves the relative folder structure. Returns the number of images written.
    """
    src_root = Path(src_root)
    dest_root = Path(dest_root)
    if not src_root.exists():
        raise FileNotFoundError(f"Source root does not exist: {src_root}")

    # create dest_root if it doesn't exist
    dest_root.mkdir(parents=True, exist_ok=True)

    # 300 dpi
    mat = fitz.Matrix(300 / 72, 300 / 72)

    written = 0
    files = sorted(src_root.rglob("*.pdf"))
    for pdf in tqdm(files):
        rel = pdf.parent.relative_to(src_root)
        out_dir = dest_root.joinpath(rel)
        out_dir.mkdir(parents=True, exist_ok=True)

        doc = fitz.open(pdf)
        try:
            for i in range(doc.page_count):
                page = doc.load_page(i)
                pix = page.get_pixmap(matrix=mat)  # pyright: ignore[reportAttributeAccessIssue]
                out_path = out_dir / f"{pdf.stem}_page_{i + 1:03d}.png"
                pix.save(str(out_path))
                written += 1
        finally:
            doc.close()

    return written


if __name__ == "__main__":
    # Edit these paths to your environment before running.
    SRC_ROOT = Path("data")
    DEST_ROOT = Path("converted_data")

    print(f"Converting PDFs in {SRC_ROOT} -> {DEST_ROOT}")
    total = convert_pdfs(src_root=SRC_ROOT, dest_root=DEST_ROOT)
    print(f"Done. Images written: {total}")
