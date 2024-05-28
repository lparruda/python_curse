# Função para solicitar e validar o input
def solicitar_input(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.strip():  # Verifica se a entrada não está vazia
            return entrada
        else:
            print("Entrada inválida. Por favor, tente novamente.")

# Solicita o ano de nascimento do usuário
nascimento = solicitar_input('Digite o ano em que você nasceu: ')

# Solicita o ano atual
ano_atual = solicitar_input('Digite o ano atual: ')

# Calcula a idade
idade = int(ano_atual) - int(nascimento)

# Exibe a idade
print('Você tem ' + str(idade) + ' anos de idade.')
