'''
Lambda Function:
    - Função anônima
    - Função sem nome
    - Função que pode ter vários argumentos, mas apenas uma expressão
    - Utilizada para funções simples
    - Utilizada para funções que serão utilizadas apenas uma vez
      
'''
def somar(x):
    result = lambda x: x + 10
    return result(x) * 10

print(somar(5))


# somar = lambda x: x + 10
# print(somar(5))
