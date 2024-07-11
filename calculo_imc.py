'''
Calculo de IMC - Índice de Massa Corporal

Qual é a altura, em cm:
Qual é o peso em kg:

Menor que 18,5 Magro
Entre 18,5 e 24,9 Normal
Entre 25,0 e 29,9 Sobrepeso
Entre 30,0 e 39,9 Obesidade
Maior que 40,0 Obesidade Grave.
'''

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

def calculo_imc():
    resultado = peso/(altura * altura)
    resultado = float("{:.2f}".format(resultado))
    print(resultado)
    if resultado <= 18.5:
        print(f'Resultado: {resultado} - Magro.')
    elif  18.5 < resultado < 25:
      print(f'Resultado: {resultado} - Normal')
    elif 25.0 <= resultado <= 29.9:
       print(f'Resultado: {resultado} - Sobrepeso')
    elif 30.0 <= resultado <= 34.9:
       print(f'Resultado: {resultado} - Obesidade Gráu I')
    elif 35 <= resultado <= 39.9:
       print(f'Resultado: {resultado} - Obesidade Gráu II')
    else:
       print(f'Resultado: {resultado} - Obesidade Gráu III')

calculo_imc()