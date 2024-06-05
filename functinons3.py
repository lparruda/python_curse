'''
Functions (Funções)

DRY - Don't Repeat Yourself.

'''

def soma(*numeros):
    resultado = 0
    for n in numeros:
        resultado += n
    return resultado

x = soma(1,3,6,8,10)
print(x)
 