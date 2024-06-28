import pandas as pd
import os


class InfoRepository:
    def __init__(self) -> None:
        self.csv_file_path = "prescriptions.csv"

    def save_openai(self, response):
        # Convert response to DataFrame
        data = {
            response.choices[0].message.content
        }
        df = pd.DataFrame(data)

        # Check if the CSV file exists
        if os.path.isfile(self.csv_file_path):
            # Append to the existing CSV file
            df.to_csv(self.csv_file_path, mode='a', header=False, index=False)
        else:
            # Create a new CSV file
            df.to_csv(self.csv_file_path, index=False)

        print(f"Response stored in {self.csv_file_path}")

    def save_gemini(self, response):
        pass
        