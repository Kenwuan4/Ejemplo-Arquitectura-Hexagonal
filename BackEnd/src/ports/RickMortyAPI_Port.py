import abc


class RickAPI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_characters_info(self, page):
        pass
