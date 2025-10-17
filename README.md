# Python Utilities

A collection of useful Python scripts for various tasks.

- [Python Utilities](#python-utilities)
  - [Modules](#modules)
    - [Image Conversion](#image-conversion)
    - [PDF Conversion](#pdf-conversion)
    - [Pydantic AI](#pydantic-ai)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation and Setup](#installation-and-setup)
  - [Usage](#usage)

## Modules

### Image Conversion

-   **`src/python_utils/image/convert_pdf_image.py`**: Converts PDF files to PNG images. It uses PyMuPDF to render PDF pages into high-resolution images (300 DPI). The script preserves the directory structure of the source PDFs.

### PDF Conversion

-   **`src/python_utils/pdf/convert_docs_to_pdf.py`**: Converts `.doc` files to PDF format using LibreOffice. It recursively searches for `.doc` files in a given directory and converts them in place.

### Pydantic AI

-   **`src/python_utils/pydanticai/init_google_agent.py`**: Initializes a Pydantic AI agent with a Google language model (e.g., Gemini). It handles loading Google Cloud credentials and configuring the agent with specific model settings.

## Getting Started

### Prerequisites

-   Python 3.12+
-   [LibreOffice](https://www.libreoffice.org/download/download/) needs to be installed and in your system's PATH for the `.doc` to PDF conversion.
-   Google Cloud credentials for the Pydantic AI agent.

### Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/python_utils.git
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

Each module can be run as a standalone script.

-   **Convert PDFs to Images**:
    -   Edit the `SRC_ROOT` and `DEST_ROOT` variables in `src/python_utils/image/convert_pdf_image.py`.
    -   Run the script: `python src/python_utils/image/convert_pdf_image.py`

-   **Convert .doc to PDF**:
    -   Place your `.doc` files in a directory (e.g., `data`).
    -   Edit the `data_dir` variable in `src/python_utils/pdf/convert_docs_to_pdf.py`.
    -   Run the script: `python src/python_utils/pdf/convert_docs_to_pdf.py`

-   **Initialize Pydantic AI Agent**:
    -   Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your Google Cloud service account JSON file.
    -   Import and use the `initialize_agent` function in your code.
