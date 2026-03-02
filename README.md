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

before:
<img width="1920" height="1080" alt="Captura de pantalla (9)" src="https://github.com/user-attachments/assets/b8996b4d-8c89-4353-949c-ac833386e7cd" />

after:
<img width="1920" height="1080" alt="Captura de pantalla (10)" src="https://github.com/user-attachments/assets/15f8f336-e240-4849-b32c-cf079c196b07" />

