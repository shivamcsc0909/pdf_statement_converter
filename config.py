import os
from pathlib import Path

# Only set Poppler path if on Windows and path exists
if os.name == 'nt':  # Windows
    poppler_paths = [
        r"C:\poppler\Library\bin",
        r"C:\poppler\bin",
        r"C:\Program Files\poppler\bin"
    ]
    for path in poppler_paths:
        if os.path.exists(path):
            os.environ["POPPLER_PATH"] = path
            break

# File paths
BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"
SAMPLE_DIR = BASE_DIR / "samples"

# Create directories if they don't exist
OUTPUT_DIR.mkdir(exist_ok=True)
SAMPLE_DIR.mkdir(exist_ok=True)

# Processing settings
MAX_FILE_SIZE_MB = 50
SUPPORTED_MIME_TYPES = ["application/pdf"]
TEMP_IMAGE_DIR = "temp_images"

# CSV output settings
CSV_ENCODING = "utf-8"
CSV_SEPARATOR = ","
DATE_FORMAT = "%Y-%m-%d"
