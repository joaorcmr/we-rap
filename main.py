from infra import EnvConfig
from external_services import AwsService, GcloudService, OpenaiService, GeminiService, ClaudeService
from repositories import InfoRepository
from models import InfoModel


def main():
  env_config = EnvConfig()

  aws_service = AwsService(env_config)
  gcloud_service = GcloudService(env_config, aws_service)
  openai_service = OpenaiService(env_config)
  gemini_service = GeminiService(env_config)
  claude_service = ClaudeService(env_config)
  info_repository = InfoRepository()
  info_model = InfoModel()
  
  imagem = info_model.IMAGE_NAMES[6]
  base64_imagem = gcloud_service.get_image_from_bucket(imagem)
  
  response_openai = openai_service.read_image(base64_imagem)
  #response_gemini = gemini_service.read_image(base64_imagem)
  response_claude = claude_service.read_image(base64_imagem)
  save_csv_openai = info_repository.save_openai(response_openai)
  save_csv_claude = info_repository.save_claude(response_claude)


if __name__ == "__main__":
  main()