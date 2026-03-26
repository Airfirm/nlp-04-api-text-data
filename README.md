# nlp-04-api_text-data

# NLP API Text Data Project

## Overview

This project builds an **EVTL pipeline** for working with API-based JSON text data.

EVTL stands for:

- **Extract** – request raw JSON data from an API
- **Validate** – inspect and confirm the JSON structure and required fields
- **Transform** – reshape the data and create analytical features
- **Load** – save the processed output for later analysis

The project uses Python and Polars to turn raw API comment data into a structured, analysis-ready dataset.

---

## Project Goal

The goal of this project is to take raw JSON data from an API and transform it into a clean tabular dataset that can support exploratory analysis and future NLP work.

This project focuses on:

- understanding JSON structure before processing
- validating required fields and data types
- transforming nested or semi-structured API data into a DataFrame
- creating derived features from text fields
- preparing data for reporting, analysis, and downstream text processing

---

## Source Data

The raw API response contains comment-style records with fields such as:

- `postId`
- `id`
- `name`
- `email`
- `body`

## Pipeline Structure

## The project is organized into separate pipeline stages:

- config_femi.py – configuration values and paths
- stage01_extract_femi.py – extracts raw JSON from the API
- stage02_validate_femi.py – validates structure and required fields
- stage03_transform_femi.py – transforms the JSON into a structured DataFrame
- stage04_load_femi.py – loads the processed data to the final output
- pipeline_api_femi_json.py – main orchestrator that runs all stages in order

Run with:

```bash
uv run python -m nlp.pipeline_api_femi_json


Custom Transformations

The transform stage was modified to match the real API structure and create analysis-ready features, including:

post_id
comment_id
email_domain
body_clean
body_preview
name_length
email_length
body_length_chars
body_length_words
line_count
is_multiline
has_long_body
Key Insight

A major lesson from this project was that raw JSON must be inspected before writing transformation logic. The example code expected userId, but the actual API returned postId, which caused a KeyError. Updating the transform stage to match the real schema made the pipeline work correctly and produced a more useful dataset for analysis.

Future Improvements

Future enhancements could include tokenization, word frequency analysis, sentiment analysis, and visualizations based on the transformed comment text.


[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project for Web Mining and Applied NLP.

Web Mining and Applied NLP focus on retrieving, processing, and analyzing text from the web and other digital sources.
This course builds those capabilities through working projects.

In the age of generative AI, durable skills are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each project follows a similar structure based on professional Python projects.
These projects are **hands-on textbooks** for learning Web Mining and Applied NLP.

## This Project

This project focuses on retrieving and processing structured text data
**from web APIs in JSON format**.

The goal is to acquire JSON data from an external source,
inspect and validate its structure,
transform it into a usable format,
and load it into a reproducible output.

You've likely heard of ETL or ELT.
We recommend EVTL.

In EVTL, each stage has a source, a process, and a sink.

- **Extract** acquires data
- **Validate** inspects and checks it
- **Transform** reshapes it
- **Load** sends it to the chosen destination

This project illustrates how to **work with real API data and understand its structure before analysis**.

## Key Files

You'll work with these files as you update authorship and experiment:

- **src/nlp/pipeline_api_json.py** - MAIN PIPELINE SCRIPT (no changes needed)
- **src/nlp/config_case.py** - Python configuration (<mark>**copy and edit**</mark> for your custom project)
- **src/nlp/stage01_extract.py** - EXTRACT (no changes needed)
- **src/nlp/stage02_validate_case.py** - VALIDATE (<mark>**copy and edit**</mark>)
- **src/nlp/stage03_transform_case.py** - TRANSFORM (<mark>**copy and edit**</mark>)
- **src/nlp/stage04_load.py** - LOAD (no changes needed)
- **pyproject.toml** - <mark>**update**</mark> authorship, links, and dependencies
- **zensical.toml** - <mark>**update**</mark> authorship and links

## First: Follow These Instructions

Follow the [step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/) to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**

## Success

After running the script successfully, you will see:


```shell
========================
Pipeline executed successfully!
========================
```

And new files will appear:

- project.log - confirming successful run
- data/raw/case_raw.json - dump of the fetched JSON
- data/processed/case_processed.csv - final loaded result

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/Airfirm/nlp-04-api-text-data
cd nlp-04-api-text-data
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
git add -A
uvx pre-commit run --all-files

# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# Later, we install spacy data model and
# en_core_web_sm = english, core, web, small
# It's big: spacy+data ~200+ MB w/ model installed
#           ~350–450 MB for .venv is normal for NLP
# uv run python -m spacy download en_core_web_sm

# First, run the module
# IMPORTANT: Close each figure after viewing so execution continues
uv run python -m nlp.pipeline_api_json

uv run ruff format .
uv run ruff check . --fix
uv run zensical build

git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Example Artifact (Output)



```text
START PIPELINE
ROOT_PATH = .
DATA_PATH = data
RAW_PATH = data\raw
PROCESSED_PATH = data\processed
========================
STAGE 01: EXTRACT starting...
========================
SOURCE PATH = https://jsonplaceholder.typicode.com/posts
SINK PATH = data\raw\case_raw.json
========================
STAGE 02: VALIDATE starting...
========================
JSON STRUCTURE INSPECTION:
Top-level type: list
Keys in first record: ['userId', 'id', 'title', 'body']
Field types:
userId: int
id: int
title: str
body: str
Validation passed.
Sink: validated JSON object
========================
STAGE 03: TRANSFORM starting...
========================
Transformation complete.
DataFrame preview:
shape: (5, 6)
...preview of dataframe...
Sink: Polars DataFrame created
========================
STAGE 04: LOAD starting...
========================
SINK PATH = data\processed\case_processed.csv
========================
Pipeline executed successfully!
========================
```


## Enhancements

In production systems, validation is often automated using tools
such as Great Expectations or Soda.

In this module, validation is implemented manually to develop a
clear understanding of structure, assumptions, and data quality.
