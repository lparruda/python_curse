valor = int(input("Digite o valor do produto: R$ "))

while valor > 20:
    valor = (valor * 0.1) + valor
    print(f"O valor do produto é R$ {valor:.2f}")
    break