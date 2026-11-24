class Foydalanuvchi:
    def __init__(self,ism,username,parol):
        self.ism = ism
        self.username = username
        self.__parol = parol

    def parolni_ozgartir(self,eski_parol, yangi_parol):
        if self.__parol == eski_parol:
            self.__parol = yangi_parol
            print("Parol mufoqiyatli o'zgartirildi!")
        else:
            print("Parol xato")

    def tekshir(self,parol):
        if self.__parol == parol:
            print("Parol tog'ri!")
        else:
            print("Parol xato kiritildi!")


o1 = Foydalanuvchi("Ali","ali_01",1234)
o2 = Foydalanuvchi("Vali","vali_06",4321)

o1.tekshir(1234)
o1.parolni_ozgartir(1234,5678)
print("====================")
o2.tekshir(1234)
o2.parolni_ozgartir(1234,7896)
