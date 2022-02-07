import abc


class Products(abc.ABC):

    @abc.abstractmethod
    def get_quantity(self):
        pass

    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def get_name(self):
        pass
