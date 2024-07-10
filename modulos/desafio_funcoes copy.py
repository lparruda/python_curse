'''
Calcular quantidade de tinta necessária para pintar
uma parede. O usuário deverá fornecer as seguintes informações:
Rendimento, altura largura.
Qual o rendimento da lata? 4
Qual a altura da parede? 2
Qual a largura da parede? 5
'''
rendimento = int(input('Rendimento: '))
altura = int(input('Altura: '))
largura = int(input('Largura: '))

def calcula_tinta():
    area = altura * largura
    result = area / rendimento
    print(f'A quantidade de tinta necessária é {result}litros.')

calcula_tinta()