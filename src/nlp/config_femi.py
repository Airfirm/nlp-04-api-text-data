"""
    config_femi.py

Purpose

  Store configuration values for the EVTL pipeline.

Analytical Questions

- What API endpoint should be used as the data source?
- What HTTP request headers are required?
- Where should raw and processed data be stored?

"""

from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================

API_URL: str = "https://jsonplaceholder.typicode.com/comments"

HTTP_REQUEST_HEADERS: dict[str, str] = {
    "User-Agent": "nlp-module-4-femi/1.0",
    "Accept": "application/json",
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

RAW_JSON_PATH: Path = RAW_PATH / "femi_raw.json"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "femi_processed.csv"
