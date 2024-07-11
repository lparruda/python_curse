carros = ['BMW','X6','Porche','Ferrari']
escolha = input('Escolha seu carro: ')

# if carros.__contains__(escolha):
#     print(f'Temos o carro {escolha}')
# else:
#     print(f'No momento não temos o carro {escolha}')
if escolha in carros:
    print(f'Temos seu carro {escolha}')
else:
    print(f'Não temos o seu carro {escolha}')
