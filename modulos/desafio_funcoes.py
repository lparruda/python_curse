'''
Calcular quantidade de tinta necessária para pintar
uma parede. O usuário deverá fornecer as seguintes informações:
Rendimento, altura largura.
Qual o rendimento da lata? 4
Qual a altura da parede? 2
Qual a largura da parede? 5
'''
class CalculaTinta():
  def __init__(self,rendimento,altura,largura):
    self.rendimento = float(rendimento)
    self.altura = float(altura)
    self.largura = float(largura)
  
  def resultado(self):
    area = self.altura * self.largura
    result = area / self.rendimento
    return result
# Obter os valores do usuário
rendimento = input('rendimento da lata: ')
altura = input('altura: ')
largura = input('largura: ')

# Criar a instância da classe
calcule1 = CalculaTinta(rendimento,altura,largura)

# Calcular e exibir o resultado
quantidade_tinta = calcule1.resultado()
print(f'A quantidade de tinta necessária é: {quantidade_tinta} litros')
