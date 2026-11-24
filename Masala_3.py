class Avtomobil:
    def __init__(self,nom):
        self.nom = nom
        self.__eshik_ochiq = 1

    def eshikni_och(self):
        if self.__eshik_ochiq == 1:
            print("Avtomabil eshik ochiq!")
        else:
            self.__eshik_ochiq = 1
            print("Avtomabil eshik ochildi")

    def eshikni_yop(self):
        if self.__eshik_ochiq == 1:
            self.__eshik_ochiq == 0
            print("Avtomabil eshiki yopildi!")
        else:
            print("Avtomabil eshik yopilgan!")

    def holat(self):
        if self.__eshik_ochiq == 1:
            print("Eshik ochiq!")
        else:
            print("Eshik yopiq!")

mashina = Avtomobil("Chevrolet Cobalt")
mashina.eshikni_och()
mashina.holat()
mashina.eshikni_yop()

