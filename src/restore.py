from .base import Base


class Import(Base):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start(self, *args, **kwargs):
        print(self.file_handler.read_data())
