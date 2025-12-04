# Python Utilities

A collection of useful Python scripts for various tasks.

- [Python Utilities](#python-utilities)
  - [Modules](#modules)
    - [Image Conversion](#image-conversion)
    - [PDF Conversion](#pdf-conversion)
    - [JSON to Excel](#json-to-excel)
    - [Pydantic AI](#pydantic-ai)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation and Setup](#installation-and-setup)
  - [Usage](#usage)
    - [CLI Commands](#cli-commands)
    - [Python API](#python-api)

## Modules

### Image Conversion

-   **`src/python_utils/image/convert_pdf_image.py`**: Converts PDF files to PNG images. It uses PyMuPDF to render PDF pages into high-resolution images (300 DPI). The script preserves the directory structure of the source PDFs.

### PDF Conversion

-   **`src/python_utils/pdf/convert_docs_to_pdf.py`**: Converts `.doc` and `.docx` files to PDF format using LibreOffice. It recursively searches for documents in a given directory and converts them in place.

### JSON to Excel

-   **`src/python_utils/json2excel/json_to_excel.py`**: Converts JSON files with nested structures to Excel spreadsheets with a flattened tabular format. Supports both single file and batch directory conversion.

### Pydantic AI

-   **`src/python_utils/pydanticai/init_google_agent.py`**: Initializes a Pydantic AI agent with a Google language model (e.g., Gemini). It handles loading Google Cloud credentials and configuring the agent with specific model settings.

## Getting Started

### Prerequisites

-   Python 3.12+
-   [LibreOffice](https://www.libreoffice.org/download/download/) needs to be installed and in your system's PATH for the `.doc`/`.docx` to PDF conversion.
-   Google Cloud credentials for the Pydantic AI agent.

### Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mfmezger/python_utils.git
    cd python_utils
    ```

2.  **Install dependencies:**
    This project uses `uv` for package management.
    ```bash
    pip install uv
    uv sync
    ```

3.  **Set up pre-commit hooks:**
    This project uses `pre-commit` to enforce code quality.
    ```bash
    pre-commit install
    ```

## Usage

### CLI Commands

After installation, use the `python-utils` CLI:

```bash
# Convert JSON to Excel
python-utils json2excel input.json -o output.xlsx
python-utils json2excel ./json_directory/ -o ./excel_output/

# Convert PDFs to images
python-utils pdf2image ./pdfs/ ./images/

# Convert .doc/.docx to PDF
python-utils doc2pdf ./documents/

# Show help
python-utils --help
```

### Python API

Import modules directly in your code:

```python
# Image conversion
from python_utils.image import convert_pdfs

convert_pdfs(src_root="./pdfs", dest_root="./images")

# JSON to Excel
from python_utils.json2excel import convert_json_to_excel

convert_json_to_excel(Path("data.json"), Path("output.xlsx"))

# Document to PDF
from python_utils.pdf import convert_docs_to_pdf

convert_docs_to_pdf("./documents")

# Pydantic AI Agent
from python_utils.pydanticai import initialize_agent

agent = initialize_agent(
    prompt="You are a helpful assistant.",
    output_model=MyOutputModel,
)
```

## License

MIT License - see [LICENSE](LICENSE) for details.
