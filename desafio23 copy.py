# Solicita ao usuário a base e o expoente
base = float(input("Digite a base: "))

# Tenta obter o expoente do usuário
expoente_input = input("Digite o expoente (pressione Enter para usar o padrão 2): ")

# Define o expoente, usando 2 como padrão se não for fornecido
if expoente_input:
    expoente = float(expoente_input)
else:
    expoente = 2

# Calcula o resultado
resultado = base ** expoente

# Exibe o resultado
print(f"{base} elevado a {expoente} é {resultado}")
