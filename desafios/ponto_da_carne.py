'''
Temperaturas  - Cozimento
120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (Bem passada)
'''

temperatuda_carne = int(input('Qual é a temperatura da carne?'))
print(temperatuda_carne)

print(f'Temperatura da carne: {temperatuda_carne}')
    
if temperatuda_carne < 48:
    print('Deixe assar mais.')
elif temperatuda_carne == 48 or temperatuda_carne < 54:
    print('Selada.')
elif temperatuda_carne == 54 or temperatuda_carne < 60:
    print('Ao ponto para o mal')
elif temperatuda_carne == 60 or temperatuda_carne < 65:
    print('Ao ponto')
elif temperatuda_carne == 65 or temperatuda_carne < 71:
    print('Ao ponto para o bem.')
elif temperatuda_carne == 71 or temperatuda_carne > 71:
    print('Bem passada.')