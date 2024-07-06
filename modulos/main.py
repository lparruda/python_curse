from functions import somar, mult
from package.cadastro import cliente



mult()
somar()

nome = cliente('Digite seu nome: ')
sobrenome = cliente('Digite seu sobrenome: ')
resposta = f'Cadastro realizado com sucesso: Nome: {nome} Sobrenome: {sobrenome}'
print(resposta)



