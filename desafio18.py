cidades = ('recife','olinda','paulista')
escolha = input('Digite uma cidade: ')

if cidades.__contains__(escolha):
    print(f'A cidade {escolha} está na lista.')
else:
    print(f'A cidade {escolha} não está na lista de cidades.')