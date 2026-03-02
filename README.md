# Clean TXT or CSV Files and Export to XLSX

A simple Python tool to clean and standardize CSV or TXT files.

## Features
- Remove empty rows and columns
- Normalize text (strip spaces, lowercase)
- Standardize empty values (`"", "<NA>", "nan"`)
- Standardize column names: lowercase, separated by underscores (`_`)

## Requirements
- Python 3.13
- pandas 2.3.3

## Usage
1. Clone or download this repository.
2. Place your CSV or TXT file in the `input` folder.
3. Run the script:

```console
python main.py
