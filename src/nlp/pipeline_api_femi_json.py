"""
    pipeline_api_femi_json.py

Purpose

  Orchestrate a standard ETL/EVTL pipeline.
  Illustrate how to extract JSON data from an API, validate it, transform it, and load it into a sink.
  Illustrate how to parse JSON to get the desired information.


Analytical Questions

- How can we extract JSON data from an API and save it to a file?
- How can we validate the structure and content of the JSON data?
- How can we transform the validated JSON data into a structured format (like a DataFrame)?
- How can we load the transformed data into a sink (like a CSV file)?



"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging

from datafun_toolkit.logger import get_logger, log_header, log_path

from nlp.config_femi import (
    API_URL,
    DATA_PATH,
    HTTP_REQUEST_HEADERS,
    PROCESSED_CSV_PATH,
    PROCESSED_PATH,
    RAW_JSON_PATH,
    RAW_PATH,
    ROOT_PATH,
)
from nlp.stage01_extract_femi import run_extract
from nlp.stage02_validate_femi import run_validate
from nlp.stage03_transform_femi import run_transform
from nlp.stage04_load_femi import run_load

# ============================================================
# Section 2. Configure Logging
# ============================================================

LOG: logging.Logger = get_logger("CI", level="DEBUG")


# ============================================================
# Section 3. Define Main Pipeline Function
# ============================================================


def main() -> None:
    log_header(LOG, "MODULE 4: EVTL PIPELINE")
    LOG.info("START PIPELINE")

    RAW_PATH.mkdir(parents=True, exist_ok=True)
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

    log_path(LOG, "ROOT_PATH", ROOT_PATH)
    log_path(LOG, "DATA_PATH", DATA_PATH)
    log_path(LOG, "RAW_PATH", RAW_PATH)
    log_path(LOG, "PROCESSED_PATH", PROCESSED_PATH)

    # EXTRACT
    json_data = run_extract(
        source_api_url=API_URL,
        http_request_headers=HTTP_REQUEST_HEADERS,
        raw_json_path=RAW_JSON_PATH,
        LOG=LOG,
    )

    # VALIDATE
    validated_data = run_validate(
        json_data=json_data,
        LOG=LOG,
    )

    # TRANSFORM
    df = run_transform(
        json_data=validated_data,
        LOG=LOG,
    )

    # LOAD
    run_load(
        df=df,
        processed_csv_path=PROCESSED_CSV_PATH,
        LOG=LOG,
    )

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")


# ============================================================
# Section 4. Run Main Function when This File is Executed
# ============================================================

if __name__ == "__main__":
    main()
