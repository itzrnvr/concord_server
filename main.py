from server import Server
from fastapi import FastAPI

server = Server()
app = server.start()


