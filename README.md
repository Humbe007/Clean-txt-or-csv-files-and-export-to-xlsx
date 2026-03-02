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
```

Before:
<img width="1920" height="1080" alt="Captura de pantalla (9)" src="https://github.com/user-attachments/assets/7b35cc3e-42e6-4563-9ccd-660a83b879c0" />

After:
<img width="1920" height="1080" alt="Captura de pantalla (10)" src="https://github.com/user-attachments/assets/a0c952f3-26d7-4c6a-be77-f9965a1bdd16" />
