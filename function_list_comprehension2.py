'''
List Comprehension
- Mais simples de escrever;
- Utilizado quando você precisa criar uma nova lista a partir de uma existente.
- [expressao for iten in itens]
'''
numeros = (x * 10 for x in range(10))
numeros2 =[x * 10 for x in range(10)]
print(list(numeros))
print('=========================')
print(numeros2)
