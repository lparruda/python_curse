def fatorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    fatorial_anterior = fatorial(n - 1)
    return n * fatorial_anterior
resultado = fatorial(4)
print(f"O fatorial de 4 é {resultado}")
