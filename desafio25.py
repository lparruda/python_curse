def fatorial(n):
    if n == 0:
        return 1
    fatorial_anterior = fatorial(n -1)
    resultado = n * fatorial_anterior
    print(f'O fatorial de {n} é {resultado}')
    return resultado
n = int(input(f'Digite um número: '))
fatorial(n)
