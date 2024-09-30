#!/opt/anaconda3/bin/python
# coding: utf-8
import shutil
from pathlib import Path
from ExpenseCommons import ExpenseCommons  # Assuming ExpenseCommons is in a separate module

class FileProcessor:
    def __init__(self, commons_inst):
        # Use ExpenseCommons for directory and file management
        self.commons = commons_inst
        self.source_path = commons_inst.get_directory_path("local", "Source")
        self.data_path = commons_inst.get_directory_path("local", "Data")
        self.backup_path = commons_inst.get_directory_path("local", "Backup")
        self.output_path = commons_inst.get_directory_path("local", "Outputs")
        self.list_of_files =[]
        self.transformed_file_list = []

    # Load the list of files from the source directory
    def load_file_list(self):
        self.list_of_files = self.commons.get_filenames(self.source_path)
        print("Loaded files:", self.list_of_files)

    # Copy files from source to output
    def copy_files_data_to_backup(self):
        for file in self.list_of_files:
            shutil.copy(self.source_path / file, self.output_path)
            # print(f"Copied {file} to {self.output_path}")

    # Transform and move files with a date appended to the filename
    def transform_file_list(self):
        for file in self.list_of_files:
            new_file_name = self.commons.add_date_to_transformed_file_name(file)
            self.transformed_file_list.append(new_file_name)
            source_file = self.source_path / file
            new_backup_file = self.backup_path / new_file_name
            shutil.move(source_file, new_backup_file)  # Rename/move file
            # print(f"Transformed {file} to {new_backup_file}")
        print(f"Transformed file names = {self.transformed_file_list}")

    # Main method to orchestrate the operations
    def main(self):
        print("Main method started")
        self.load_file_list()  # Load file list
        self.copy_files_data_to_backup()  # Copy files
        self.transform_file_list()  # Optionally transform files
        print("Main method finished")


# Ensures that the main method is executed when the script is run directly
if __name__ == "__main__":
    root_path = "/Users/sergiofaro/PycharmProjects/expenses"  # Set the root path here
    commons = ExpenseCommons(root_path)  # Create an instance of the ExpenseCommons class
    processor = FileProcessor(commons)  # Create an instance of the FileProcessor class
    processor.main()  # Call the main method
