from src.base import Base


class Export(Base):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start(self, *args, **kwargs):
        resp = self.session.get(self.default_folder_children)
        self.file_handler.write_data(self.__get_all_folder(4, []))

    def __get_all_folder(self, data, collected_data):
        resp = self.session.get(self.folder_by_id(data))
        collected_data.extend(resp.json())
        for element in resp.json():
            id_of_folder = element.get('id')
            self.__get_all_folder(id_of_folder, collected_data)
        return collected_data
