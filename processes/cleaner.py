import pandas as pd
import re

def normalize_columns(df):
    """
This function normalizes column names to snake_case using .lower().
It removes any character that is not a letter, number, or '_'.
    """
    df_corrected = df.copy()
    mapping = {}
    
    original = df_corrected.columns.tolist()
    
    for col in original:
        correct_col = col.lower()
        correct_col = re.sub(r"[^a-z0-9áéíóú]+", "_", correct_col)
        correct_col = re.sub(r"_+", "_", correct_col)
        correct_col = correct_col.strip("_") 
        mapping[col] = correct_col                                  
    df_corrected.rename(columns= mapping, inplace= True)
    
    return df_corrected

def remove_duplicate_rows_and_columns(df):
    """
Removes duplicate rows and columns with all duplicate data.
    """
    clean_df = df.copy()
    clean_df = clean_df.drop_duplicates()
    clean_df = clean_df.loc[: , ~clean_df.T.duplicated()] 

# df.loc[rows, columns] returns the DataFrame of the selected rows and columns.
# : selects all columns, and ~clean_df.T.duplicated returns a boolean series of the non-duplicate columns for selection.
# Note: .duplicated() always checks for identical rows, and what we do is transpose with .T to check for identical columns instead.

    return clean_df

def clean_strings(df):
    """
This function selects columns of type object and applies .strip() and .lower() to them.
It also replaces empty values with pandas <NA>.
    """
    df_string_cleaned = df.copy()
    
    text_cols = df_string_cleaned.select_dtypes(include="object").columns    
    
    for col in text_cols:
        df_string_cleaned[col] = df_string_cleaned[col].str.strip()
        df_string_cleaned[col] = df_string_cleaned[col].str.lower()
        df_string_cleaned[col] = df_string_cleaned[col].replace({"nan": pd.NA, "<NA>": pd.NA, "": pd.NA})
    
    return df_string_cleaned

def eliminate_empty_data(df):
    """
This function removes completely empty columns and rows.
    """
    df_copy = df.copy()
    df_copy.dropna(axis=1, how="all", inplace=True)    
    df_copy.dropna(axis=0, how="all", inplace=True)
    
    return df_copy
    
        
    


def clean(df):
    """
This function calls all the functions from the cleaner module and executes them on the received DataFrame. 
df = normalize_columns(df)
df = remove_duplicate_rows_and_columns(df)
df = eliminate_empty_data(df)
df = clean_strings(df)    
    """
    df_cleaned = df.copy()
    df_cleaned = normalize_columns(df_cleaned)
    df_cleaned = remove_duplicate_rows_and_columns(df_cleaned)
    df_cleaned = clean_strings(df_cleaned)
    df_cleaned = eliminate_empty_data(df_cleaned)
    
    return df_cleaned





