import os
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from router import RegisterRouterList
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    # 实例化
    app = FastAPI()

    # 跨域，*代表所有
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 注册路由
    for item in RegisterRouterList:
        app.include_router(item)

    # 加载静态资源
    app.mount(
        "/static",
        StaticFiles(directory=os.path.join(os.getcwd(), "static")),
        name="static",
    )

    return app
