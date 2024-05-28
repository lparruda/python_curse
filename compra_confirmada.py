compra_comfirmada=False
dados_da_compra = 'Compra no valor R$300,00 e entrega confirmada.'
for enviar in range(3):
    if compra_comfirmada:
      print(dados_da_compra)
      break
else:
      print('Compra não realizada.')