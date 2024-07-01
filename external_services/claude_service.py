import anthropic
from infra import EnvConfig

class ClaudeService:
    def __init__(self, env_config: EnvConfig) -> None:
        key = env_config.get_env("CLAUDE_API_KEY")
        
        self.key = key
        self.client = anthropic.Anthropic(api_key=self.key)
    
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
        - PDF or picture 

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
        Pdf or picture:
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
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=2048,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": base64_image,
                            },
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ],
                }
            ],
        )
        print(message.content[0])
        return message.content[0].text
