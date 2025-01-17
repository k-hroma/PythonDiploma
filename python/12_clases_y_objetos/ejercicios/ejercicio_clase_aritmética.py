class Aritmetica():
    def __init__(self, operando1, operando2):
        self._operando1 = operando1
        self._operando2 = operando2

    def sumar(self,):
        print(f"El resultado de la suma es = {self._operando1 + self._operando2}")

    def restar(self,):
        print(f"El resultado de la resta es = {self._operando1 - self._operando2}")

    @property
    def operando1(self,):
        print(f"Valor actual: {self._operando1}")
        return self._operando1

    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1
        print(f"Nuevo valor: {self._operando1}")

    @property
    def operando2(self,):
        print(f"Valor actual: {self._operando2}")
        return self._operando2

    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2
        print(f"Nuevo valor: {self._operando2}")


aritmetica1 = Aritmetica(9, 2)
aritmetica1.operando1
aritmetica1.operando2
aritmetica1.sumar()
aritmetica1.restar()
aritmetica1.operando1 = 10
aritmetica1.operando2 = 4
aritmetica1.sumar()
aritmetica1.restar()
setattr(aritmetica1, "operando3", 5)
print(aritmetica1.__dict__)
print(aritmetica1.operando3)
aritmetica1.operando4 = 8
print(aritmetica1.__dict__)
print(aritmetica1.operando4)