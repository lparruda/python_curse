def somar():
    print('Está função vai somar')

def mult():
    print('Está função vai multiplicar')

def find_index(lista, item):
    for i, valor in enumerate(lista):
        if valor == item:
          return i
    return -1