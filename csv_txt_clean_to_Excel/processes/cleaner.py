import pandas as pd
import re


def normalize_columns(df):
    """
This function normalizes column names to snake_case using .lower().
It removes any character that is not a letter, number, or '_'.
    """
    mapping = {}
    original = df.columns.tolist()
    for col in original:
        correct_col = col
        correct_col = correct_col.strip().lower()                   
        correct_col = re.sub("( )", "_",correct_col)
        correct_col = re.sub("([^a-z0-9_áéíóú]+)","",correct_col)   
        mapping[col] = correct_col                                  
    df.rename(columns= mapping, inplace= True)
    df_corrected = df
    return df_corrected

def remove_duplicate_rows_and_columns(df):
    """
Removes duplicate rows and columns with all duplicate data.
    """

    clean_df = df.drop_duplicates()
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
    text_cols = df.select_dtypes(include="object").columns    
    for col in text_cols:
        df[col] = df[col].str.strip()
        df[col] = df[col].str.lower()
        df[col] = df[col].replace({"nan": pd.NA, "<NA>": pd.NA, "": pd.NA})
    
    return df

def eliminate_empty_data(df):
    """
This function removes completely empty columns and rows.
    """
    df.dropna(axis=1, how="all", inplace=True)    
    df.dropna(axis=0, how="all", inplace=True)
    
    return df
    
        
    


def clean(df):
    """
This function calls all the functions from the cleaner module and executes them on the received DataFrame. 
df = normalize_columns(df)
df = remove_duplicate_rows_and_columns(df)
df = eliminate_empty_data(df)
df = clean_strings(df)    
    """
    
    df = normalize_columns(df)
    df = remove_duplicate_rows_and_columns(df)
    df = eliminate_empty_data(df)
    df = clean_strings(df)
    
    return df

