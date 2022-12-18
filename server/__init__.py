from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .paths import homeRouter, authRouter, chatRouter


class Server:
    def __init__(self):
        self.app = None
        self.routers = [homeRouter, authRouter, chatRouter]

    def start(self):
        self.app = FastAPI()
        self.__initCordMiddleWare()
        self.__includeRouters()
        return self.app

    def __includeRouters(self):
        for router in self.routers:
            self.app.include_router(router)

    def __initCordMiddleWare(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
