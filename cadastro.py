def f_input(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.strip():
            return entrada
        else:
            print('Erro! Digite conforme solicitado.')
        
nome = f_input('Digite seu nome: ')
sobrenome = f_input('Digite seu sobrenome: ')
resposta = f'Cadastro realizado com sucesso: Nome: {nome} Sobrenome: {sobrenome}'
print(resposta)