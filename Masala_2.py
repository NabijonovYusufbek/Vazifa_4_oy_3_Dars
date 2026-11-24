class Kitob:
    def __init__(self,nom,muallif):
        self.nom = nom
        self.muallif = muallif
        self.__ijarada = 1

    def ijaraga_ber(self):
        self.__ijarada -= self.__ijarada
        print("Kitob ijaraga berildi!")

    def qaytarish(self):
        if self.__ijarada == 0:
            self.__ijarada = 1
            print("Ijaradagi kitob qytarildi!")
        else:
            print("Kitob joyida turibdi!")

    def holat(self):
        if self.__ijarada == 1:
            print("Kitob bor!")
        else:
            print("Kitob ijaraga berilgan!")

k1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy")
k1.ijaraga_ber()
k1.holat()
k1.qaytarish()
    
