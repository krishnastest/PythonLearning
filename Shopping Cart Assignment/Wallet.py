import abc


class Wallet(abc.ABC):

    @abc.abstractmethod
    def getwalletbalance(self):
        pass

    @abc.abstractmethod
    def addwalletbalance(self):
        pass

    @abc.abstractmethod
    def deductamount(self):
        pass


