from infra import EnvConfig
from external_services import AwsService, GcloudService, OpenaiService, GeminiService, ClaudeService
from repositories import InfoRepository


def main():
  env_config = EnvConfig()

  aws_service = AwsService(env_config)
  gcloud_service = GcloudService(env_config, aws_service)
  openai_service = OpenaiService(env_config)
  gemini_service = GeminiService(env_config)
  claude_service = ClaudeService(env_config)
  info_repository = InfoRepository()

  imagem_name = '1686074729322112700_IgNhja5u.png'
  base64_imagem = gcloud_service.get_image_from_bucket(imagem_name)
  #encode_image = claude_service.encode_image(base64_imagem)
  #response_openai = openai_service.read_image(base64_imagem)
  #response_gemini = gemini_service.read_image(base64_imagem)
  response_claude = claude_service.read_image(base64_imagem)
  #save_csv_openai = info_repository.save_openai(response_openai)
  save_csv_claude = info_repository.save_claude(response_claude)
  #print(response_openai.choices[0].message.content)
  


if __name__ == "__main__":
  main()