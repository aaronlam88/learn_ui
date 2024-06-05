# learn_ui

## Description

Learn JavaScript and Python. We will use Python to collect data, do some ML, and build a server using FastAPI. JavaScript will be used to build our UI. We will use React Native framework to build the UI.

## Table of Contents

- [Setup Instructions](#setup-instructions)
  - [Clone the Repository](#clone-the-repository)
  - [Create and Activate Virtual Environment](#create-and-activate-virtual-environment)
  - [Install Requirements](#install-requirements)
- [Data Collector](#data-collector)
  - [Prepare JSON File](#prepare-json-file)

## Setup Instructions

Follow these steps to set up the project environment.

### Clone the Repository

```bash
git clone https://github.com/aaronlam88/learn_ui.git
cd learn_ui
```

### Create and Activate Virtual Environment

```bash
# Create virtual environment named .venv
python -m venv .venv

# Activate virtual environment
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

## Data Collector

First, let build data collector so we can have the data we need. `data_collection.py` script will fetches historical data for symbols listed in the snp500.json file using the Yahoo Finance API (yfinance) and saves the data to CSV files.

### Prepare JSON File

Ensure you have a JSON file named `snp500.json` in the data_collection directory with the list of symbols and other relevant information. We can download this data from [Data Hub S&P 500](https://datahub.io/core/s-and-p-500-companies), and save to `snp500.json`

Example JSON structure:

```json
[
    {
        "Symbol": "AAPL",
        "Company": "Apple Inc.",
        "Industry": "Technology",
        "Exchange": "NASDAQ"
    },
    {
        "Symbol": "MSFT",
        "Company": "Microsoft Corporation",
        "Industry": "Technology",
        "Exchange": "NASDAQ"
    },
    ...
]
```

### Run the Script

Navigate to the data_collection directory and run the `data_collector.py` script:

```bash
cd data_collection
python data_collector.py
```

The script will fetch historical data for each symbol listed in `snp500.json` and save it as CSV files in the 'data' directory.
