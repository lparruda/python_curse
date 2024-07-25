# lista = [1,2,3,4,5]
# for n in lista:
#     quadrado = n ** 2
#     print(f'O quadrado de {n} é {quadrado}')
# lista = [1, 2, 3, 4, 5]
# resultados = list(map(lambda n: f'O quadrado de {n} é {n ** 2}', lista))
# for resultado in resultados:
#     print(resultado)
lista = [1,2,3,4,5]

result = []
for n in lista:
    result.append(n ** 2)
print(f'O quadrado da lista {lista} é {result}')
