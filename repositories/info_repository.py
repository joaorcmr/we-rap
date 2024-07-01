import pandas as pd
import os


class InfoRepository:
    def __init__(self) -> None:
        self.csv_file_path_openai = "prescriptions1.csv"
        self.csv_file_path_claude = "prescriptions3.csv"

    def save_openai(self, response):
        data = {
            response
        }
        df = pd.DataFrame(data)

        if os.path.isfile(self.csv_file_path_openai):
            df.to_csv(self.csv_file_path_openai, mode='a', header=False, index=False)
        else:
            df.to_csv(self.csv_file_path_openai, index=False)

        print(f"Response stored in {self.csv_file_path_openai}")

    def save_claude(self, response):
        data = {
            response
        }
        df = pd.DataFrame(data)

        if os.path.isfile(self.csv_file_path_claude):
            df.to_csv(self.csv_file_path_claude, mode='a', header=False, index=False)
        else:
            df.to_csv(self.csv_file_path_claude, index=False)

        print(f"Response stored in {self.csv_file_path_claude}")
        