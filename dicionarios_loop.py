'''
    Dicionários
      Utiliza index no formato de keys e values.
      Aceita string, integer, float, boolean...
'''

aluno = {'nome': 'Ana',
         'idade': 16, 
         'nota': 9.5, 
         'aprovação': True, 
         'materias': ['matemática', 'português', 'física']}
#aluno.pop('idade')
#del aluno['idade']

# for keys, values in aluno.items():
#     print(keys, values)
print(aluno.keys())
print(aluno.values())
print(len(aluno['materias']))
