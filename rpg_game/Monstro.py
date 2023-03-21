from Ser_vivo import Ser_vivo

class Monstro(Ser_vivo):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.tipo = tipo
        
    