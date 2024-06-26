from infra import EnvConfig
from .aws_service import AwsService
import json
from google.cloud import storage
import base64


class GcloudService:
  def __init__(self, env_config: EnvConfig, aws_service: AwsService) -> None:
    bucket= env_config.get_env('GCLOUD_BUCKET_NAME')
    json_credential_key = env_config.get_env('AWS_JSON_CREDENTIAL_KEY')
    json_credential = aws_service.get_secret_string(json_credential_key)
    json_credential_data = json.loads(json_credential)

    self.bucket = bucket
    self.aws_service = aws_service
    self.storage_client = storage.Client.from_service_account_info(json_credential_data)

  def get_image_from_bucket(self, file_name: str) -> str:
    bucket = self.storage_client.bucket(self.bucket)
    blob = bucket.blob(file_name)
    content = blob.download_as_bytes()

    return base64.b64encode(content).decode('utf-8')