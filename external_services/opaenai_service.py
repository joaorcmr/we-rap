from infra import EnvConfig
import requests


class OpenaiService:
  def __init__(self, env_config: EnvConfig) -> None:
    key = env_config.get_env("OPENAI_API_KEY")
    url = env_config.get_env("OPENAI_URL")

    self.key = key
    self.url = url

  def read_image(self, base64_image: str):
    payload = {
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Whats in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}
    headers = {
     "Content-Type": "application/json",
  "Authorization": f"Bearer {self.key}"
    }


    response = requests.post(self.url, headers=headers, json=payload)
    
    if response.status_code == 200:
      return response.json()
    
    print("text", response.text)
    print("status", response.status_code)
    return 
