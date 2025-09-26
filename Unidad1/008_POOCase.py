class Cuenta_Bancaria:
    def __init__(self, titular, saldo=0):
        self.titular=titular
        self.saldo=saldo


    def depositar(self, cantidad):   
        
        self.saldo +=cantidad
        print(f"{self.titular} ha depositado ${cantidad}. Saldo actual: ${self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo disponible insuficiente.")
        else:
            self.saldo-=cantidad
            print(f"{self.titular} retiro ${cantidad}. Saldo actual${self.saldo}")
    def consultar_saldo(self):
        print(f" El saldo actual de {self.titular} es:  ${self.saldo}")

class Cuenta_premiun(Cuenta_Bancaria):
    def __init__(self, titular, saldo=0, sobregiro=50000):
       super().__init__(titular, saldo)
       self.sobregiro=sobregiro

    def retirar(self, cantidad):
        if cantidad > self.saldo + self.sobregiro:
            print("Saldo insufieciente")
        else:
            self.saldo -= cantidad
            print(f"{self.titular} retiro ${cantidad}. Saldo actual ${self.saldo} Sobregiro disponible ${self.sobregiro+(self.saldo if self.saldo<0 else 0)}")


cuenta1= Cuenta_Bancaria("Kevin Suárez", 50000)
cuenta1.depositar(2800)
cuenta1.consultar_saldo()
cuenta1.retirar(26000)


cuenta2=Cuenta_premiun("Cristian Suarez", 150000)
cuenta2.depositar(50000)
cuenta2.retirar(260000)
cuenta2.consultar_saldo() 
cuenta2.retirar(250000)

