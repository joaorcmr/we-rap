from infra import EnvConfig
import boto3


class AwsService:
  def __init__(self, env_config: EnvConfig) -> None:
    region = env_config.get_env("AWS_REGION")
    key = env_config.get_env("AWS_KEY")
    secret = env_config.get_env("AWS_SECRET")
  
    self.secret_manager_client = boto3.client(
       'secretsmanager',
        region_name=region,
        aws_access_key_id=key,
        aws_secret_access_key=secret
    )

  def get_secret_string(self, secret_id: str) -> str:
    response = self.secret_manager_client.get_secret_value(SecretId=secret_id)
    return response['SecretString']