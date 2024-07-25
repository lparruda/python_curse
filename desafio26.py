def num1(n):
  resultado = n * n
  print(f'O quadrado de {n} é {resultado}')
  return resultado
def num2(resultado):
  resultado1 = resultado * resultado
  print(f'O quadrado de {resultado} é {resultado1}')
  return resultado1


n = int(input('Digite um número: '))
resultado = num1(n)
num2(resultado)


# print(f'O quadrado de {n} é {num1(n)}')
# print(f'')

