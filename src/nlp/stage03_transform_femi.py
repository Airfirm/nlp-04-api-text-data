"""
stage03_transform_femi.py
(EDIT YOUR COPY OF THIS FILE)

Source: validated JSON object
Sink: Polars DataFrame

Purpose

  Transform validated JSON data into a structured format.

Analytical Questions

- Which fields are needed from the JSON data?
- How can records be normalized into tabular form?
- What derived fields would support analysis?

Notes

Following our process, do NOT edit this _case file directly,
keep it as a working example.

In your custom project, copy this _case.py file and
append with _yourname.py instead.

Then edit your copied Python file to:
- extract the fields needed for your analysis,
- normalize records into a consistent structure,
- create any derived fields required.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
import re
from typing import Any

import polars as pl

# ============================================================
# Section 2. Define Run Transform Function
# ============================================================


def run_transform(
    json_data: list[dict[str, Any]],
    LOG: logging.Logger,
) -> pl.DataFrame:
    """Transform JSON into a structured DataFrame with analytical features.

    Args:
        json_data (list[dict[str, Any]]): Validated JSON data.
        LOG (logging.Logger): The logger instance.

    Returns:
        pl.DataFrame: The transformed dataset.
    """
    LOG.info("========================")
    LOG.info("STAGE 03: TRANSFORM starting...")
    LOG.info("========================")

    records: list[dict[str, Any]] = []

    for record in json_data:
        # Safe extraction
        post_id = record.get("postId")
        comment_id = record.get("id")
        name = str(record.get("name", "")).strip()
        email = str(record.get("email", "")).strip()
        body = str(record.get("body", "")).strip()

        # Clean body text for later text analysis
        body_clean = re.sub(r"\s+", " ", body.replace("\n", " ")).strip()

        # Derived analytical fields
        email_domain = email.split("@")[1].lower() if "@" in email else None
        name_length = len(name)
        email_length = len(email)
        body_length_chars = len(body)
        body_length_words = len(body_clean.split()) if body_clean else 0
        line_count = len(body.splitlines()) if body else 0
        is_multiline = line_count > 1
        has_long_body = body_length_words > 20
        body_preview = body_clean[:60]

        records.append(
            {
                "post_id": post_id,
                "comment_id": comment_id,
                "name": name,
                "email": email,
                "email_domain": email_domain,
                "body": body,
                "body_clean": body_clean,
                "body_preview": body_preview,
                "name_length": name_length,
                "email_length": email_length,
                "body_length_chars": body_length_chars,
                "body_length_words": body_length_words,
                "line_count": line_count,
                "is_multiline": is_multiline,
                "has_long_body": has_long_body,
            }
        )

    df: pl.DataFrame = pl.DataFrame(records)

    # Optional: sort for easier reading
    df = df.sort(["post_id", "comment_id"])

    LOG.info("Transformation complete.")
    LOG.info(f"Shape: {df.shape}")
    LOG.info(f"Columns: {df.columns}")
    LOG.info(f"DataFrame preview:\n{df.head()}")
    LOG.info("Sink: Polars DataFrame created")

    return df
