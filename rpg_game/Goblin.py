from Monstro import Monstro

class Goblin(Monstro):
    def __init__(self, tipo, pontos_de_vida, pontos_de_ataque, inteligencia):
        super().__init__(tipo, pontos_de_vida, pontos_de_ataque)
        self.inteligencia = inteligencia

    
        