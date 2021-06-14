import configparser


class Connection(object):
    """Class provides the connection between server and request-suffixes

    """

    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read('config/connection.ini')

    @property
    def auth_data(self):
        """Property provides authentication data. These are necessary to connect and get data

        :return: tuple for auth=(<user>,<pw>) at request
        """
        return self.__config['credentials']['user'], self.__config['credentials']['password']

    @property
    def url(self):
        """Property provides the url where all calls start and uri will be created

        :return: url
        """
        return ''.join([self.__config['connection']['host'], self.__config['connection']['api_entry']])
