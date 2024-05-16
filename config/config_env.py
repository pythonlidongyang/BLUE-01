import os
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    app_env: str
    app_port: int
    app_host: str
    app_version: str
    app_reload: bool

    class Config:
        env_path = os.environ.get("ENV", "development")  # 第二个参数可设定环境默认值，不填返回None
        env_file = f"config/{env_path}.env"
