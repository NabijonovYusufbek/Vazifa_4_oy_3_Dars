# Abrstarct - mavhum
from abc import ABC,abstractmethod

class Hayvon:
    @abstractmethod
    def ovoz(self):
        pass


class Mushuk(Hayvon):
    def ovoz(self):
       print("Mushuk: Miyov!")


class It(Hayvon):
    def ovoz(self):
        print("It: vov-vov!")

m1 = Mushuk()
m1.ovoz()
it1 = It()
it1.ovoz()