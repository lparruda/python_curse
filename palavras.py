# numeros = [2,3,4,5]
nomes = ['Ana', 'Bia', 'Cris', 'Duda', 'Eva', 'Fê', 7, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

item, item1, item5, *outros  = nomes


for i in nomes:
    print(f'Os valores para imprimir são:{i}')

# # numeros = [2, 3, 4, 5]
# nomes = ['Ana', 'Bia', 'Cris', 'Duda', 'Eva', 'Fê', 7, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# item, item1, *outros, item5 = nomes

# print(item)   # Ana
# print(item1)  # Bia
# print(item5)  # Fê
# print(outros) # ['Cris', 'Duda', 'Eva', 7, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
