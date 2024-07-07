from datetime import datetime
# Criar classe

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    
    def idade(self):
        ano = datetime.now().year    
        return  ano - self.ano_nascimento

# Criar Objeto

usuario1 = Funcionarios('Luciano', 'Pereira', 1978)
usuario2 = Funcionarios('Taciana', 'Alencar', 1982)
usuario3 = Funcionarios('Vitor', 'Pereira', 2007)

# Print
print(f'Usuário:{usuario1.nome},Idate:{Funcionarios.idade(usuario1)}')
print(f'Usuário:{usuario2.nome},Idade:{Funcionarios.idade(usuario2)}')
print(f'Usuário:{usuario3.nome},Idade:{Funcionarios.idade(usuario3)}')

