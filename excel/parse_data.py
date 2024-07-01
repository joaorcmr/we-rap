import json
import pandas as pd


class DataToExcel:
    def __ini__(self):
        pass

    def parse_data_openai(self):
        data = pd.read_csv("/prescriptions1.csv")

        # Parse the JSON content in each row
        parsed_data = []
        for index, row in data.iterrows():
            parsed_row = json.loads(row[0])
            parsed_data.append(parsed_row)

        # Create a new DataFrame from the parsed data
        parsed_df = pd.DataFrame(parsed_data)

        # Save the new DataFrame to an Excel file
        excel_path = '/mnt/data/prescriptions_parsed.xlsx'
        parsed_df.to_excel(excel_path, index=False)

        excel_path


    def parse_data_claude(self):
        # Load the CSV file again
        data_new = pd.read_csv("/prescriptions3.csv")

        # Parse the JSON content in each row and gather 'interpretation' keys
        parsed_data_new = []
        for index, row in data_new.iterrows():
            parsed_row = json.loads(row[0])
            interpretation = parsed_row.pop('interpretation', {})
            parsed_row.update(interpretation)
            parsed_data_new.append(parsed_row)

        # Create a new DataFrame from the parsed data
        parsed_df_new = pd.DataFrame(parsed_data_new)

        # Save the new DataFrame to an Excel file
        excel_path_interpretation = '/mnt/data/prescriptions_parsed_with_interpretation.xlsx'
        parsed_df_new.to_excel(excel_path_interpretation, index=False)

        excel_path_interpretation
