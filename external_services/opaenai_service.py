from infra import EnvConfig
import requests


class OpenaiService:
  def __init__(self, env_config: EnvConfig) -> None:
    key = env_config.get_env("OPENAI_API_KEY")
    url = env_config.get_env("OPENAI_URL")

    self.key = key
    self.url = url

  def read_image(self, base64_image: str):
    prompt = f"""
      You are an AI assistant tasked with reading and interpreting medical prescriptions. This is a critical task that requires attention to detail and careful consideration of all information provided. Your goal is to accurately interpret the prescription and provide clear, concise information that can be easily understood by healthcare professionals and patients.
      You will be provided with an image of a medical prescription and some basic patient information. Here is the prescription image:
      <prescription_image>
      {base64_image}
      </prescription_image>
      Please follow these steps to analyze and interpret the prescription:
      Carefully examine the prescription image. Look for the following elements:
      Patient name
      Date of prescription
      Prescriber's name and signature
      Drug name(s)
      Dosage(s)
      Route of administration
      Frequency of administration
      Quantity prescribed
      Number of refills (if any)
      Any special instructions or warnings
      Interpret the prescription by considering:
      The legibility of the handwriting
      Any abbreviations or medical shorthand used
      Potential drug interactions or contraindications
      Appropriate dosage based on standard medical guidelines
      Consider the provided patient information in relation to the prescription. Look for any potential issues such as:
      Age-related concerns
      Known allergies
      Existing medical conditions that may interact with the prescribed medication
      Provide your interpretation of the prescription in the following format:
      {{
          "Patient Name": "",
          "Date of Prescription": "",
          "Prescriber": "",
          "Medication(s)": [
              {{
                  "Drug Name": "",
                  "Dosage": "",
                  "Route": "",
                  "Frequency": "",
                  "Quantity": "",
                  "Refills": "",
                  "Special Instructions": ""
              }}
          ],
          "Concerns or Potential Issues": "",
          "Additional Notes": ""
      }}
      Remember:
      If any part of the prescription is illegible or unclear, note this in your interpretation.
      If you identify any potential errors or concerns (e.g., unusual dosage, drug interactions), highlight these in the "Concerns or Potential Issues" section.
      Do not make assumptions about illegible or missing information. If you cannot read or understand something, state that it is unclear.
      If you need to use medical terminology, provide a brief explanation in layman's terms where possible.
      IMPORTANT: Never guess or invent information that is not clearly provided in the prescription image or patient information. Your role is to interpret the given information accurately, not to make medical judgments or recommendations.
    """

    headers = {
      "Authorization": f"Bearer {self.key}",
      "Content-Type": "application/json"
    }

    data = {
      "prompt": prompt,
    }

    response = requests.post(self.url, headers=headers, json=data)

    if response.status_code == 200:
      return response.json()
    
    print("text", response.text)
    print("status", response.status_code)
    return 
