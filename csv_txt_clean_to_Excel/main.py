from sys import exit as sys_exit
from processes import loader as lo
from processes  import cleaner as cl
from processes import export as ex


#       -----       Part 1: loader      -----

in_folder = "input"

try:
    file = lo.file_path_from_folder(in_folder)

except FileNotFoundError as e:
    
    print(e)
    lo.create_folder(in_folder)
    print("The input folder has been created.")
    sys_exit(input(f"""The folder {in_folder} is empty, please add a txt or csv file ready to be processed.
Press enter to finish.
"""))
 
except IndexError as e:
    
    print(e)
    lo.create_folder(in_folder)
    sys_exit(input(f"""The folder {in_folder} is empty, please add a txt or csv file ready to be processed.
Press enter to finish.
"""))
 
    
except ValueError as e:
    sys_exit(input(f"""{e}
Press Enter to Finish.
"""))


file_path = lo.get_file_path_from_folder(in_folder)
print("Received File path.")
    

try:
    type_file = lo.txt_or_csv(file_path)
    print(f"File .{type_file} detected correctly.")

except ValueError as e:
    sys_exit(input(f"{e}\nPress Enter to finish.\n"))

try:

    df = lo.get_df_from_file_path(file_path)

except UnicodeDecodeError:
  sys_exit(input("""ERROR: The file encoding is not supported.
Please export the file as UTF-8 or standard CSV from Excel.
Press Enter to finish.
"""))
except ValueError as e:
    sys_exit(input(f"{e}\nPress Enter to finish.\n"))
print("The file has been charged.")

try:
    lo.data_validation_for_df(df)
except ValueError as e:
    print(e)

try:
    lo.validate_not_empty(df)
except ValueError as e:
    sys_exit(input(f"""{e}
Press Enter to Finish.
"""))

#       -----       Part 2: Cleaner      ------

df = cl.clean(df)
print("The file has been cleaned.")

#       -----       Part 4: Output      ------

out_folder = "output"

try:
    ex.df_to_excel(df,out_folder,file_path)
except ValueError as e:
    print(e)
    lo.create_folder(out_folder)
    

input("""The file has been exported successfully.
Press Enter to Finish.
""")
