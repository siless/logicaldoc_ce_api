import logging
import requests

from lib.connection import Connection
from lib.file_handler import DataFileHandler


class Base(object):

    def __init__(self, *args, **kwargs):
        self.conn = Connection()
        logging.basicConfig(filename='log/logicaldoc.log', level=logging.DEBUG)
        self.session = requests.Session()
        self.session.auth = self.conn.auth_data
        self.default_folder_children = self.conn.url + 'folder/listChildren?folderId=4'

        self.content_type_json = {'content_type': 'application/json'}
        self.file_handler = DataFileHandler()

    def start(self, *args, **kwargs):
        raise NotImplementedError

    def folder_by_id(self, id):
        """Method creates url to get data of folder by id

        :param id: id of folder
        :return: str
        """
        return self.conn.url + f'folder/listChildren?folderId={id}'
