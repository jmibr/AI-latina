class funciones:

    def __init__(self, pow2,pow3,mod2,mod1):
        self.pow2=pow2
        self.mod2=mod2
        self.pow3=pow3
        self.mod1=mod1
    def cuadrado(self, pow2):
        return self.pow2**2
    def tercero(self, pow3):
        return self.pow3**3
    def modulo(self, mod2, mod1):
        return self.mod2%mod1
