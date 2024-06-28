from infra import EnvConfig
import requests
import pandas as pd
import os
import google.generativeai as genai

class GeminiService:
    def __init__(self, env_config: EnvConfig) -> None:
        self.key = env_config.get_env("GAMINEE_API_KEY")
        self.url = env_config.get_env("GAMINEE_URL")
        
        
        genai.configure(api_key=self.key)


    def read_image(self, base64_image: str):
        prompt = """
        You are an AI assistant tasked with reading and interpreting medical prescriptions. This is a critical task that requires attention to detail and careful consideration of all information provided. Your goal is to accurately interpret the prescription and provide clear, concise information that can be easily understood by healthcare professionals and patients.
        
        You will be provided with an image of a medical prescription. Here is the prescription image:
        
        Please follow these steps to analyze and interpret the prescription:
        Carefully examine the prescription image. Look for the following elements:
        - Patient name
        - Date of prescription
        - Prescriber's name and signature
        - Drug name(s)
        - Dosage(s)
        - Route of administration
        - Frequency of administration
        - Quantity prescribed
        - Number of refills (if any)
        - Any special instructions or warnings
        - Doctor CRM
        - Doctor ocupation
        - Stamp (True or false)

        Interpret the prescription by considering:
        - The legibility of the handwriting
        - Any abbreviations or medical shorthand used
        - Potential drug interactions or contraindications
        - Appropriate dosage based on standard medical guidelines

        Provide your interpretation of the prescription in the following format:
        <interpretation>
        Patient Name:
        Date of Prescription:
        Prescriber:
        Doctor CRM:
        Doctor Ocupation:
        Stamp (True or false):
        Medication(s):
        [Drug Name]
        Dosage:
        Route:
        Frequency:
        Quantity:
        Refills:
        Special Instructions:
        [If there are multiple medications, repeat the above structure]
        Concerns or Potential Issues:
        Additional Notes:
        </interpretation>

        Remember:
        - If any part of the prescription is illegible or unclear, note this in your interpretation.
        - If you identify any potential errors or concerns (e.g., unusual dosage, drug interactions), highlight these in the "Concerns or Potential Issues" section.
        - Do not make assumptions about illegible or missing information. If you cannot read or understand something, state that it is unclear.
        - If you need to use medical terminology, provide a brief explanation in layman's terms where possible.
        - IMPORTANT: Never guess or invent information that is not clearly provided in the prescription image or patient information. Your role is to interpret the given information accurately, not to make medical judgments or recommendations.
        - Return the message in JSON format, exclude </interpretation>
        - Remove Json markdown in the message 
        """
        
        payload = {
            "model": "gaminee-model",
            "prompt": prompt,
            "image": base64_image,
            "max_tokens": 3000
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}"
        }

        response = requests.post(self.url, json=payload, headers=headers)
        
        if response.status_code == 200:
            json_response = response.json()
            self.store_response_in_csv(json_response)
            return json_response
        
        return None

    def store_response_in_csv(self, response):
        # Convert response to DataFrame
        data = {
            "content": [response["content"]]
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
