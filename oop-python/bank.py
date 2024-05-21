from abc import *

class Bank(ABC):
    @abstractmethod
    def cal_bal(self):
        pass


# we can create object for abstract class

# Bank() - TypeError: Can't instantiate abstract class Bank with abstract method cal_bal