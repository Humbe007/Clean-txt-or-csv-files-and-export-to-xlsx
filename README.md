# Clean CSV Files and Export to Excel (XLSX)

A simple Python tool to clean, filter, and standardize CSV or Excel files, then export them to Excel.

## Features

* Remove empty rows and columns
* Normalize text (strip spaces, lowercase)
* Standardize empty values (`"", "<NA>", "nan"`)
* Standardize column names: lowercase, separated by underscores (`_`)
* Filter rows using conditions like `"column" "operator" "value"`
* Export the cleaned data to Excel (`.xlsx`)

## Requirements

* Python 3.13
* pandas 2.3.3

## Usage

1. Clone or download this repository.

2. Place your CSV file in the `input` folder.

3. (Optional) Define filters in the script using the format:
```python
filters = [
    ("column_name", "operator", "value")
]
```
Example:
```python
filters = [
    ("city", "==", "cdmx"),
    ("age", ">", 18)
]
```
4. Run the script:
```console
python main.py
```
The cleaned and filtered file will be exported to the `output` folder as an Excel (`.xlsx`) file.

## Example

Input CSV:
```
city,age
cdmx,25
guadalajara,17
```
Filter:
```
("age", ">", 18)
```
Output Excel:
```
city,age
cdmx,25
```
