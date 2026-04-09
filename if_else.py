numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
import random

precisao = int(input("Precisão (0-100): "))
elemento_arma = input("Elemento (Fogo/Gelo/Fisico): ")

#a biblioteca random faz com que possamos definif uma variavel aleatoria nesse caso é (sorte)

sorte = random.randint(1, 100)
inimigo = {"elemento": "Gelo", "fraqueza": "Fogo"}
base = 10

#criei um if para continuar o processo do calculo de dano

if random.randint(0, 100) < precisao:
    mult = 2 if (elemento_arma == "Fogo" and inimigo["elemento"] == "Gelo") else 1.5 if (elemento_arma == inimigo["fraqueza"]) else 1
    dano_final = base * mult
    
    if mult > 1: print("Super Efetivo!")
    
    if sorte > 95:
        dano_final *= 2
        print(f"CRÍTICO! (Sorte rolada: {sorte})")
        
    print(f"Acertou! Dano total: {dano_final}")
else:
    print("Errou!")
