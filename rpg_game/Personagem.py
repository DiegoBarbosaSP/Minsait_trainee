from Ser_vivo import Ser_vivo

class Personagem(Ser_vivo):
    def __init__(self, pontos_de_vida, pontos_de_ataque,nome):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.nome = nome

    