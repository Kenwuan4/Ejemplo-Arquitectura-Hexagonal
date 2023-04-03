import abc


class Persistance_port(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_email(self, email):
        pass

    @abc.abstractmethod
    def autenticate_user(self, email, password):
        pass

    @abc.abstractclassmethod
    def save(self, email, password):
        pass
