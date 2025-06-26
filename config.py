import os
from pathlib import Path
os.environ["POPPLER_PATH"] = r"C:\poppler\Library\bin"
os.environ["POPPLER_PATH"] = "C:\\poppler\\bin"
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
