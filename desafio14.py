idade = int(input('Digite sua idade: '))
if idade < 13:
    print(f'Idade: {idade}, você é uma criança.')
elif  13 <= idade <=19:
    print(f'Idade: {idade}, você é um adolescente.')
else:
    print(f'Você é um adulto.')