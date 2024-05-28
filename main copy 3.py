def s_input(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.strip():
            return entrada
        else:
            print('Erro! Digite conforme solicitado.')
nome = s_input('Digite seu nome: ')
sobrenome = s_input('Digite seu sobrenome')
resposta = f'Seu nome é {nome} e seu sobrenome é {sobrenome}. Obrigado {nome} {sobrenome}.'

print(resposta)