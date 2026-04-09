
soma = 0

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    
    if numero == 0:
        break  # Sai do laço imediatamente
    
    soma += numero  # É o mesmo que soma = soma + numero

print(f"A soma total é: {soma}")
