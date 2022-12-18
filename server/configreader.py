import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.json')


class ConfigReader:
    def __init__(self):
        pass

    def baseApi(self):
        return self.read()["baseApi"]

    def read(self):
        file = open(CONFIG_PATH)
        dat = json.loads(file.read())
        file.close()
        return dat

