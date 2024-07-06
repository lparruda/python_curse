def cliente(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.strip():
            return entrada
        else:
            print('Erro! Digite conforme solicitado.')
        
# nome = cliente('Digite seu nome: ')
# sobrenome = cliente('Digite seu sobrenome: ')
# resposta = f'Cadastro realizado com sucesso: Nome: {nome} Sobrenome: {sobrenome}'
# print(resposta)