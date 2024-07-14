def expoent(num1, num2=2):
    return num1 ** num2

base = int(input('Digite a base: '))
expoente = input('Digite o expoente: ')

if expoente:
   expoente = int(expoente)
   print(f'{base} elevado a {expoente} é igual a {expoent(base,expoente)}')
else:
   print(f'{base} elevado a 2 é igual a {expoent(base)}')




