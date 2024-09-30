#!/opt/anaconda3/bin/python
# coding: utf-8

import datetime
from pathlib import Path
import pandas as pd

class ExpenseCommons:
    LAST_DATE_STR = '2024-07-30'
    INPUT_FILE = "accountactivity-3.csv"

    def __init__(self, root_path):
        self.root_path = Path(root_path)
        self.final_file_list = ([], [])

    @staticmethod
    def today_date():
        current_date = datetime.date.today()
        date_str = current_date.strftime("%Y-%m-%d")
        return date_str

    @staticmethod
    def get_current_year_month():
        current_date = datetime.date.today()
        year_month = current_date.strftime("%Y_%m")
        return year_month

    def get_directory_path(self, base, directory_value):
        if base == "local":
            self.root_path = Path("/Users/sergiofaro/PycharmProjects/expenses")
        elif base == "cloud":
            self.root_path = Path("/Users/sergiofaro/Library/Mobile Documents/com~apple~CloudDocs/VSCode/expenses")
        else:
            raise ValueError("Path not found or provided")

        if directory_value == "Source":
            return self.root_path / "Source"
        elif directory_value == "Outputs":
            return self.root_path / "Outputs"
        elif directory_value == "Data":
            return self.root_path / "Data"
        elif directory_value == "Backup":
            return self.root_path / "Backup"
        else:
            raise ValueError("Directory has not been defined")

    @staticmethod
    def get_transformed_file_name(input_file):
        file_map = {
            "accountactivity.csv": "TD_chequing",
            "accountactivity-2.csv": "TD_Saving",
            "accountactivity-3.csv": "TD_Aeroplan",
            "accountactivity-4.csv": "TD_LOC",
            "statement.csv": "BMO_chequing",
            "cibc.csv": "CIBC_MCard",
        }
        return file_map.get(input_file, "No filename provided")

    def get_input_file_path(self, input_file):
        filepath = self.get_directory_path("local", "Source")
        return filepath / input_file

    def add_date_to_transformed_file_name(self, file_name):
        file_date = self.today_date()  # Call static method without self
        return f"{file_name}_{file_date}.csv"

    def add_year_month_to_transformed_file_name(self, file_name):
        year_month = self.get_current_year_month()  # Call static method without self
        return f"{file_name}_{year_month}.csv"

    def read_and_save_dataframe_from_input_file(self, input_file_name):
        full_path_input = self.get_input_file_path(input_file_name)
        df = pd.read_csv(full_path_input)
        return df

    def save_transformed_file_to_backup_dir(self, input_file_name):
        df = self.read_and_save_dataframe_from_input_file(input_file_name)
        full_path_save = self.get_directory_path("local", "Backup")
        transformed_filename = self.get_transformed_file_name(input_file_name)
        transformed_filename_with_date = self.add_date_to_transformed_file_name(transformed_filename)
        df.to_csv(full_path_save / transformed_filename_with_date)
        print(f"DataFrame saved as {transformed_filename_with_date}")

    def get_filenames(self, directory):
        return [
            file.name for file in Path(directory).iterdir()
            if file.is_file() and not file.name.startswith('.')
        ]

    def read_input_files_and_process(self):
        dir_path = self.get_directory_path("local", "Source")
        file_list = self.get_filenames(dir_path)
        transformed_file_list = [self.get_transformed_file_name(file) for file in file_list]
        print("New File Names:", transformed_file_list)
        self.final_file_list = [file_list, transformed_file_list]
        return self.final_file_list

    def main(self):
        print("\n********** Main Function **********")
        print(f"Input File: {self.INPUT_FILE}")

        dir_path = self.get_directory_path("local", "Source")
        transformed_file_name = self.get_transformed_file_name(self.INPUT_FILE)
        print(f"Transformed File Name: {transformed_file_name}")

        transformed_file_name_with_date = self.add_date_to_transformed_file_name(transformed_file_name)
        print(f"Transformed File Name with Date: {transformed_file_name_with_date}")

        year_month = self.get_current_year_month()
        print(f"Year_Month: {year_month}")

        year_month_file_name = self.add_year_month_to_transformed_file_name(transformed_file_name)
        print(f"Year_Month File Name: {year_month_file_name}")

        list_of_files = self.get_filenames(dir_path)
        print(f"List of Files: {list_of_files}")

        final_file_list = self.read_input_files_and_process()
        print(f"Final File List: {final_file_list}")
        print(f"Original File: {final_file_list[0][0]}")
        print(f"Transformed File: {final_file_list[1][0]}")

if __name__ == "__main__":
    root_path = "/Users/sergiofaro/PycharmProjects/expenses"
    processor = ExpenseCommons(root_path)
    processor.main()
