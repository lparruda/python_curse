# Criar classe 
class Usuarios:

# Criar objetos
    pass

    def __init__(self, nome, sobrenome, ano_nascimento): 
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

# Atribuir valores

user1 = Usuarios('Taciana', 'Alencar', '1982')
user2 = Usuarios('Luciano', 'Pereira', '1982')

print(user1.nome)
print(user1.sobrenome)
print(user1.ano_nascimento)
print(user2.nome)
print(user2.sobrenome)
print(user2.ano_nascimento)
