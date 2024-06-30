import google.generativeai as genai
import os
from infra import EnvConfig
import base64


class GeminiService:
    def __init__(self, env_config: EnvConfig) -> None:
        self.key = env_config.get_env("GEMINI_API_KEY")
        self.url = env_config.get_env("GEMINI_URL")
        self.model = genai.GenerativeModel('gemini-1.5-pro')
        self.api = genai.configure(api_key=self.key)
        self.prompt = """
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

    def read_image(self, file_path):
        with open(file_path, "rb") as image_file:
            self.base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')
        mime_type = "image/png"  # Adjust as necessary based on your image file type
        return {
            "inlineData": {"data": self.base64_encoded_data, "mimeType": mime_type}
        }

    def run(self, file_paths):
        image = self.base64_encoded_data
        result = self.model.generate_content([self.prompt], image)
        print(result)
        return result