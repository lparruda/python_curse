cores = ['amarelo', 'verde', 'preto', 'azul', 'laranja']

user = input('Digite uma cor: ')

if user.lower() in cores:
    print('Sim')
else:
    print('Não')