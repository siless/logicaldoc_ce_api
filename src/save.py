from src.base import Base


class Export(Base):
    """Conducting all operations that are necessary to export logicaldoc´s data
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start(self, *args, **kwargs):
        """Entrypoint of self

        :param args: args
        :param kwargs: kwargs
        :return: None
        """
        self.file_handler.folder_metadata = self.__get_folders_metadata(4, [])
        self.file_handler.file_metadata = self.__get_files_metadata(self.file_handler.folder_metadata)
        for content in self.__get_files_content(self.file_handler.file_metadata):
            self.file_handler.file_content(content)

    def __get_folders_metadata(self, data, collected_data):
        """Retrieving all data of directories and  their children. It retrieves no content

        :param data: id of parent-folder
        :param collected_data: reference of data that stores content of requests´ response
        :return: list of metadata
        """
        resp = self.session.get(self.folder_by_id(data))
        collected_data.extend(resp.json())
        for element in resp.json():
            id_of_folder = element.get('id')
            self.__get_folders_metadata(id_of_folder, collected_data)
        return collected_data

    def __get_files_metadata(self, data):
        """Fetching all metadata of files given by folder id

        :param data: content of 'folder_metadata.json'
        :return: list of metadata
        """
        retval = []
        for i in data:
            resp = self.session.get(self.file_by_folder_id(i.get('id')))
            retval.extend(resp.json())
        return retval

    def __get_files_content(self, data):
        """Get content of files given by their docId

        :param data: content of 'file_metadata.json'
        :return: dict
        """
        for i in data:
            resp = self.session.get(self.file_content_by_document_id(i.get('id')))
            yield {'file': i.get('fileName'), 'content': resp.content}
