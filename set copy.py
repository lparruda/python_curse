funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turno_noite = {'Pedro', 'Sophia', 'Bruno'}
tem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

# Lista 1: Funcionários que têm carro e trabalham à noite
tem_carro_noite = list(turno_noite & tem_carro)

# Lista 2: Funcionários que têm carro e trabalham durante o dia
tem_carro_dia = list(turno_dia & tem_carro)

# Lista 3: Funcionários que não têm carro
nao_tem_carro = list(funcionarios - tem_carro)

print("Lista 1 - Funcionários que têm carro e trabalham à noite:", tem_carro_noite)
print("Lista 2 - Funcionários que têm carro e trabalham durante o dia:", tem_carro_dia)
print("Lista 3 - Funcionários que não têm carro:", nao_tem_carro)
