quantidade = int(input("Quantas notas deseja inserir? "))
soma = 0

for i in range(1, quantidade + 1):
    nota = float(input(f"Digite a nota {i}: "))
    soma += nota

media = soma / quantidade
print(f"\nA média final é: {media:.2f}")
