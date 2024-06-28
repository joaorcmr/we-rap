from infra import EnvConfig
from external_services import AwsService, GcloudService, OpenaiService, GeminiService
from repositories import InfoRepository


def main():
  evn_config = EnvConfig()

  aws_service = AwsService(evn_config)
  gcloud_service = GcloudService(evn_config, aws_service)
  openai_service = OpenaiService(evn_config)
  gemini_service = GeminiService(evn_config)
  info_repository = InfoRepository()

  imagem_name = '1686074729322112700_IgNhja5u.png'
  base64_imagem = gcloud_service.get_image_from_bucket(imagem_name)
  response_openai = openai_service.read_image(base64_imagem)
  #response_gemini = gemini_service.read_image(base64_imagem)

  save_csv_openai = info_repository.save_openai(response_openai)
  
  print(response_openai.choices[0].message.content)
  


if __name__ == "__main__":
  main()