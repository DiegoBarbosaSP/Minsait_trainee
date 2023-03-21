class Ser_vivo:
    def __init__(self, pontos_de_vida, pontos_de_ataque) :
        self.pontos_de_vida = pontos_de_vida
        self.pontos_de_ataque = pontos_de_ataque

     
    def atacar(self, alvo):
        alvo.receber_dano(self.pontos_de_ataque)

    def receber_dano(self, dano):
        self.pontos_de_vida -= dano
       