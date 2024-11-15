class Partido:
    contador = 0
    def __init__(self, eq_local, eq_visitante, ptos_local, ptos_visitante):
        self.eq_local = eq_local
        self.eq_visitante = eq_visitante
        self.ptos_local = ptos_local
        self.ptos_visitante = ptos_visitante
        
    def __str__(self):
        return f"{self.eq_local}: {self.ptos_local} - {self.eq_visitante}: {self.ptos_visitante}"

    @classmethod
    def get_contador(c):
        return f"El numero de partidoses: {c.contador}"