from datetime import datetime
# Criando classe
class User:
    def __init__(self, nome, sobrenome, nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    def idade(self):
        ano_atual =  datetime.now().year
        return ano_atual - self.nascimento

# Criar objeto
#user1 = User()
#user2 = User()
# Parâmetros
user1 = User('Luciano', 'Pereira',1978)
user2 = User('Taciana', 'Alencar', 1982)

# Print
print(f'Nome:{user1.nome}, Nascimento:{user1.nascimento}')
print(f'Nome:{user2.nome}, Nascimento:{user2.nascimento}')
print(f'Nome completo:{User.nome_completo(user1)}, Idade:{User.idade(user1)}')
print(f'Nome completo:{User.nome_completo(user2)}, Idade:{User.idade(user2)}')