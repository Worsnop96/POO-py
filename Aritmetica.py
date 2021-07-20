class Aritmetica:
    def __init__(self, op1= 0, op2= 0):
        self.a = op1
        self.b = op2

    def suma(self):
        return self.a+self.b

calculadora= Aritmetica(5,8)
print(calculadora.suma())
