from abc import ABC,abstractmethod

class Xabar:
    @abstractmethod
    def yuborish(self,matn):
        pass


class Email(Xabar):
    def yuborish(self, matn):
        print("Email orqali xabar yuborildi:",matn)


class SMS(Xabar):
    def yuborish(self, matn):
       print("SMS orqali xabar yuborildi:",matn)


e1 = Email()
e1.yuborish("Salom!")
s1 = SMS()
s1.yuborish("Dars boshlandi!")
