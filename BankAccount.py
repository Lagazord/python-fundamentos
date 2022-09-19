class CuentaBancaria:

    def __init__(self, tasa_interes, balance):
        self.tasa=tasa_interes
        self.balance=balance

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
        return self

    def generar_interes(self):
        self.balance += self.balance*self.tasa
        return self

cuenta1 = CuentaBancaria(0.125, 2000)
cuenta2 = CuentaBancaria(0.125, 3000)

cuenta1.deposito(400).deposito(300).deposito(700).retiro(3000).generar_interes().mostrar_info_cuenta()
cuenta2.deposito(500).deposito(600).retiro(800).retiro(500).retiro(200).generar_interes().mostrar_info_cuenta()