
from Personagem import Personagem
from Lobo import Lobo



personagem = Personagem(100, 10, "Besta")
lobo = Lobo(50, 20, "Fera", 15)


personagem.atacar(lobo)
print(f"{lobo.tipo} recebeu {personagem.pontos_de_ataque} de dano e tem {lobo.pontos_de_vida} pontos de vida restantes.")


lobo.atacar(personagem)
print(f"{personagem.nome} recebeu {lobo.pontos_de_ataque} de dano e tem {personagem.pontos_de_vida} pontos de vida restantes.")