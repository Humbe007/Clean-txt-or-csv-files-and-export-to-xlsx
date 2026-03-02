import os
import pandas as pd
import re


def adjust_column_dimensions(worksheet):
    """
Receives a worksheet and adjusts the width of each column based on the widest data in the column, plus 2.
    """    
    for column in worksheet.columns: 
        
        max_width = 0
        col_letter = column[0].column_letter
        
        
        for line in column:
            
            value = str(line.value)
            current_width = len(value)
                
            if current_width > max_width:
                max_width = current_width
        

            
        worksheet.column_dimensions[col_letter].width = max_width + 2
            
def create_a_unique_name(output_folder, output_file_extension, input_file_path):
    """
Receives an 'output_folder', which is the folder where we want to export a new file.

The function adds f'_file_{counter}{output_file_extension}' 
to the name of the file we add in 'input_file_path' to make it  a unique name.

If the counter value already exists, it increments it by 1. 
This ensures that every file has a different name.

This function is intended to be used inside export functions. 
For that reason, it also receives the export file extension 
to append it to the output path.
    """
    
    if not os.path.isdir(output_folder):
        raise ValueError("Output folder does not exist.") 


    counter = 0
    filename = re.sub(r'.*[\\/]', '', input_file_path)
    base_name = re.sub(r'\.[^.]+$', '', filename)

    if not output_file_extension.startswith("."):
        output_file_extension = "." + output_file_extension
    
    output_file_path = os.path.join(output_folder,f"{base_name}_file_{counter}{output_file_extension}") 
     
    while os.path.exists(output_file_path):
        
        counter += 1
        output_file_path = os.path.join(output_folder,f"{base_name}_file_{counter}{output_file_extension}") 
        
    return output_file_path

    
def df_to_excel(df,output_folder,file_path):
    """
Receives a DataFrame to be exported to the specified output folder.
Uses the adjust_column_dimensions() function to adjust the column widths. 
    """

            
    output_file_path = create_a_unique_name(output_folder,".xlsx",file_path)

    with pd.ExcelWriter(output_file_path, engine = "openpyxl") as writer:
        df.to_excel(writer,sheet_name= "Sheet1", index= False)
            
        worksheet = writer.sheets["Sheet1"]
        adjust_column_dimensions(worksheet)
        
        worksheet.freeze_panes = "A2"


        