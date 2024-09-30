#!/opt/anaconda3/bin/python
# coding: utf-8
import MyCommons
from MyCommons import *
import shutil

# TODO create method for copy and renaming
# form BANK -> SOURCE
# from SOURCE transform and add date and copy to DATA
# from DATA copy to Backup

source_path = root_path / "Source"
data_path = root_path / "Data"
backup_path = root_path / "Backup"
output_path = root_path / "Outputs"
list_of_files = []


def load_file_list():
    global list_of_files
    list_of_files = MyCommons.get_filenames(source_path)
    print(list_of_files)


def copy_files_data_to_backup():
    shutil.copy(source_path, output_path)

# for sublist in two_dimensional_list:
#     # Iterating over each element in the current sublist
#     for element in sublist:
#         print(element)
# def transform_file_list():
# for file in list_of_file:
# new_file_name = add_date_to_transformed_file_name(file)
# source_path = source_path / file
# backup_path =  backup_path / new_file_name
# current_path.rename(new_path)

# load_file_list()

def main():
    print("Main method started")
    load_file_list()  # Call the method to load file list
    # You can add more function calls here if needed
    # For example: copy_files_data_to_backup()
    print("Main method finished")


if __name__ == "__main__":
    main()
