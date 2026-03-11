import os
from pandas import read_csv
from pandas.errors import EmptyDataError
# Este archivo contiene las funciones de la primera parte del proyecto, se encargan del proceso de asegurar que la 
# carpeta contenga un solo archivo txt o csv y que este no este vacío, el proposito de estas funciones es generar el dataframe listo para ser procesado.

 
# This file contains the functions from the first part of the project. They handle the process of ensuring that the folder 
# contains only one txt or csv file and that it is not empty. The purpose of these functions is to generate a DataFrame ready for processing.
 
def file_path_from_folder(folder):
    """
    This function expects the folder to contain only one file; if not, it throws an error.  
    It returns the file_path of the file inside the folder.
    """
    try:
        files = os.listdir(folder) 
    except FileNotFoundError:
        raise FileNotFoundError(f"The folder {folder} doesn't exist.")

    if len(files) == 0:
        raise IndexError(f"The folder {folder} is empty.")

    if len(files) > 1:
        raise ValueError("The folder has too many files. Expected: 1.")
    

    file = files[0] 
    return os.path.join(folder,file)
 
 
def create_folder(folder):
    "This function create a folder"
    os.makedirs(folder,exist_ok=True)
    
    
def get_file_path_from_folder(folder):
    """
    This function expects the folder to contain only one file; if not, it throws an error.  
    It returns the file_path of the file inside the folder.
    """
    files = os.listdir(folder)
    
    if len(files) > 1:
        raise ValueError("The folder has too many files. Expected: 1.")
    if len(files) == 0:
        raise ValueError(f"The folder {folder} is empty.")
    
    file = files[0]
    file_path = os.path.join(folder,file)
    return file_path


def txt_or_csv(file_path):
    """
    This function returns 'txt' or 'csv' depending on the file type.
    """
    
    file_path = file_path.lower()
    
    if file_path.endswith("txt"):
        return "txt"
    elif file_path.endswith("csv"):
        return "csv"
    else:
        raise ValueError("Incorrect file type. Please provide only .txt or .csv files.")
    
    
def get_df_from_file_path(file_path):
    """
    This function returns a copy of a DataFrame generated from the file path provided..
    """
    
    txt_or_csv(file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError("Input file not found.")
    
    try:
        df = read_csv(
            file_path,
            encoding="utf-8",
            on_bad_lines="skip")
        
    except UnicodeDecodeError:
        df = read_csv(
            file_path,
            encoding="latin-1",
            on_bad_lines="skip")
        
    except EmptyDataError:
        raise ValueError("The file is empty. Have not been found columns inside the file. Please change the file.")
    
    if df.empty:
        raise ValueError("The file is empty. The columns have no data. Please change the file.")
    
    df_copy = df.copy()
    return df_copy


def data_validation_for_df(df): 
    """
    Check the number of columns; if it equals 1, then issue a warning that only one column was detected.
    """
    if df.shape[1] == 1:
        raise ValueError("Warning: Only a single column was detected, and the file may have been read incorrectly. The result is likely not as expected.")


def validate_not_empty(df):
    """
    Check that the file is not empty.
    """
    if df.empty:
        raise ValueError("The file is empty.")