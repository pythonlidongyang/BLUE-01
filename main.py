import uvicorn
from config.config_env import Settings
from app import create_app
from functools import lru_cache

app = create_app()


# 加载环境
@lru_cache()
def get_settings():
    return Settings()


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=get_settings().app_port, reload=True, workers=1)
