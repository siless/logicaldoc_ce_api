import json
import logging


class DataFileHandler(object):

    def __init__(self):
        self.__folder = 'data/folder_metadata.json'
        self.__file = 'data/file_metadata.json'
        self.__file_content = None

    @property
    def folder_metadata(self):
        """Reading response of data/folder_medata.json

        :return: dict
        """
        with open(self.__folder) as f:
            data = json.load(f)
        return data

    @folder_metadata.setter
    def folder_metadata(self, data):
        """Writing response to data/folder_medata.json

        :param data: content
        :return: None
        """
        with open(self.__folder, 'w') as f:
            json.dump(data, f, indent=4)

    @property
    def file_metadata(self):
        """Reading content of data/file_medata.json

        :return: dict
        """
        with open(self.__file) as f:
            data = json.load(f)
        return data

    @file_metadata.setter
    def file_metadata(self, data):
        """Writing response to data/file_medata.json

        :param data: content
        :return: None
        """
        with open(self.__file, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def file_content(cls, data):
        """Writing file content

        :param data: dict
        :return: None
        """
        file = 'data/' + data.get('file')
        with open(file, 'wb') as f:
            f.write(data.get('content'))
            logging.info(f'exported: {file} ')
