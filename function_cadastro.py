def s_input(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.strip():
            return entrada
        else:
            print('Digite um valor.')

nome=s_input('Digite seu nome: ')
sobrenome= s_input('Digite seu sobrenome: ')
result=f'Seu nome é {nome} {sobrenome}.'
print(result)


nascimento=s_input('Digite o ano em que vc nasceu: ')
ano_atual=s_input('Digite o ano atual: ')
idade= int(ano_atual) - int(nascimento)
print('Você tem ' + str(idade) + ' anos de idade.')