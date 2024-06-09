'''
List Comprehension
- Mais simples de escrever;
- Utilizado quando você precisa criar uma nova lista a partir de uma existente.
- [expressao for iten in itens]
'''
frutas = ['maçã', 'banana', 'laranja', 'melancia', 'abacaxi']
frutas2 = [ iten for iten in frutas if 'b' in iten ]
# lambda x: x in 'l'
#frutas2.append(list(filter(lambda x: 'l' in x frutas)))
#frutas2.extend(filter(lambda x: 'l' in x, frutas))

print(frutas2)

# frutas = ['maçã', 'banana', 'laranja', 'melancia', 'abacaxi']
# frutas2 = list(filter(lambda x: 'l' in x, frutas))
# print(frutas2)
# for iten in frutas:
#     if 'l' in iten:
#         frutas2.append(iten)
# print(frutas2)
