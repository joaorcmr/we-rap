from dotenv import load_dotenv
import os


class EnvConfig:
  def __init__(self) -> None:
    load_dotenv()

  def get_env(self, key: str) -> str:
    return os.getenv(key)