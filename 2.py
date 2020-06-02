from abc import ABC, abstractmethod


class Clother(ABC):
    @abstractmethod
    def result(self):
        pass


class Suit(Clother):
    def __init__(self, v):
        self.v = v

    @property
    def result(self):
        val_1 = 2 * self.v + 0.3
        return val_1


class Coat(Clother):
    def __init__(self, h):
        self.h = h

    @property
    def result(self):
        val_2 = self.h / 0.65 + 0.5
        return val_2


clother_1 = Suit(170)
clother_2 = Coat(46)
print(clother_1.result)
print(clother_2.result)
print(clother_1.result + clother_2.result)
