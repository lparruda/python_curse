'''
Criar um programa que gera 3 listas:
Lista 1 = Funcionários que tem carro e trabalham a noite
Lista 2 = Funcionários que tem carro e trabalham durante o dia
Lista 3 = Funcionários que não tem carro
'''
funcionarios = ['Ana','Marcos','Alice','Pedro','Sophia','Bruno','Melissa']
turno_dia = ['Ana','Marcos','Alice','Melissa']
turno_noite = ['Pedro','Sophia','Bruno']
tem_carro = ['Marcos','Alice','Bruno','Melissa']

tem_carro_noite = set(turno_noite).intersection(tem_carro)
tem_carro = set(tem_carro)
tem_carro_dia = set(turno_dia).intersection(tem_carro)
funcionarios = set(funcionarios)
sem_carro = set(funcionarios).difference(tem_carro)

# tem_carro_noite = list(tem_carro & turno_noite)
# tem_carro_dia = list(tem_carro & turno_dia)


print(f'Funcionários da noite que tem carro:{tem_carro_noite}')
print(f'Funcionários do dia que tem carro:{tem_carro_dia}')
print(f'Funcionários que não tem carro:{sem_carro}')
