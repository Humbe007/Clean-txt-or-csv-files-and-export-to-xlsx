import pandas as pd

def definite_type_of_columns(df, columns_and_value):
    """This function takes a DataFrame and a list of tuples with column names and values, 
    and converts the columns to the appropriate data types based on the values provided.
    Expected columns_and_value format: [(column1, value1), (column2, value2), ...] where value can be a type or a string indicating the type."""
    
    df_corrected = df.copy()
    
    for column, value in columns_and_value:
        
        if column not in df_corrected.columns:
            raise KeyError(f"Column '{column}' not found in DataFrame")
        
        if value=="num" or value==int or value==float:
            df_corrected[column] = pd.to_numeric(df[column], errors='coerce')
        
        elif value=="str" or value==str:
            df_corrected[column] = df[column].astype(str)
        
        elif value=="bool" or value==bool:
            df_corrected[column] = df[column].astype(bool)
            
        elif value=="datetime" or value==pd.Timestamp:
            df_corrected[column] = pd.to_datetime(df[column], errors='coerce', dayfirst=True) 
            # Assuming day-first format for dates, adjust as needed
            
        else:
            raise ValueError(f"Unsupported data type for column '{column}': {value}")
        
    return df_corrected

def filter_data(df, filters):
    """
    Filter a DataFrame based on a list of conditions.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame to filter.

    filters : list of tuples
        Conditions in the form:
        [(column, operator, value), ...]

        Supported operators:
        ==, !=, >, <, >=, <=, in, not in

    Returns a pandas.DataFrame

    """

    if not isinstance(filters, (list, tuple)):
        raise TypeError("filters must be a list of tuples")

    df_filtered = df.copy()

    for condition in filters:

        if len(condition) != 3:
            raise ValueError(f"Invalid filter format: {condition}")

        column, op, value = condition

        if column not in df_filtered.columns:
            raise KeyError(f"Column '{column}' not found in DataFrame")

        if op == "==":
            df_filtered = df_filtered[df_filtered[column] == value]

        elif op == "!=":
            df_filtered = df_filtered[df_filtered[column] != value]

        elif op == ">":
            df_filtered = df_filtered[df_filtered[column] > value]

        elif op == "<":
            df_filtered = df_filtered[df_filtered[column] < value]

        elif op == ">=":
            df_filtered = df_filtered[df_filtered[column] >= value]

        elif op == "<=":
            df_filtered = df_filtered[df_filtered[column] <= value]

        elif op == "in":
            df_filtered = df_filtered[df_filtered[column].isin(value)]

        elif op == "not in":
            df_filtered = df_filtered[~df_filtered[column].isin(value)]

        else:
            raise ValueError(f"Unsupported operator: {op}")

    return df_filtered
