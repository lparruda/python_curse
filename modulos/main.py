tem_carne = int(input('Digite a temperatura da carne: '))

if tem_carne < 48:
    print('Deixe assar por mais alguns minutos.')
elif tem_carne in range(48,54):
    print('Selada')
elif tem_carne in range(54,60):
    print('Ao ponto para o mal.')
elif tem_carne in range(60,65):
    print('Ao ponto.')
elif tem_carne in range(65,71):
    print('Ao ponto para o bem.')
elif tem_carne >= 71:
    print('Bem passada.') 