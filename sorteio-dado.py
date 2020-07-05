import random
import time

class SorteioDado:

    def Inicio(self):
        self.resp1 = input("Deseja rolar o dado?(S/N)").upper()

        if self.resp1 == "S":
            self.RodandoDado()
        elif self.resp1 == "N":
            print("Fechando Programa")
        else:
            print("O valor digitado é diferente de S ou N")
            SorteioDado().Inicio()
        
    def RodandoDado(self):
        print('Jogando...')
        time.sleep(1)
        self.valor_dado = random.randint(1,6)
        print(self.valor_dado)
        SorteioDado().Inicio()


SorteioDado().Inicio() 

