from infra import EnvConfig
from external_services import AwsService, GcloudService, OpenaiService


def main():
  evn_config = EnvConfig()

  aws_service = AwsService(evn_config)
  gcloud_service = GcloudService(evn_config, aws_service)
  openai_service = OpenaiService(evn_config)

  imagem_name = '1686074729322112700_IgNhja5u.png'
  base64_imagem = gcloud_service.get_image_from_bucket(imagem_name)
  response_openai = openai_service.read_image(base64_imagem)

  print(response_openai)


main()