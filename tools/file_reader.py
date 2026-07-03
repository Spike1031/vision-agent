import json


class FileReader:

    def read_json(self, path):

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)