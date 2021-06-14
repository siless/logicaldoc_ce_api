import json
import logging


class DataFileHandler(object):

    def write_data(self, data):
        with open('data/data.json', 'w') as f:
            json.dump(data, f, indent=4)

    def read_data(self):
        with open('data/data.json') as f:
            data = json.load(f)
        return data
