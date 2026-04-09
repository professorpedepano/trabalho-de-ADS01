import random

hpinimigo = 100
elementoarma = input("Elemento (Fogo/Gelo): ")

while hpinimigo > 0:
    dano = 0
    if random.randint(0, 2) < 80:  # Precisão tem que ser maior de 80 para prosseguir
        # Dano se multiplica se fogo der dano a gelo assim tendo ataquem em sequencia
        mult = 2 if (elementoarma == "Fogo") else 1
        dano = (10 * mult) * (2 if random.randint(1, 100) > 95 else 1)
        hpinimigo -= dano
        print(f"Golpeou! Dano: {dano} HP Inimigo: {max(0, hpinimigo)}")
    else:
        print("Errou!")
if hpinimigo == 0:
    print("Inimigo derrotado!")
    
