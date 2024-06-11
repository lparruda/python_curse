from datetime import datetime
class Usuarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    def idade(self):
        return datetime.now().year - int(self.ano_nascimento)

user1 = Usuarios('Luciano', 'Pereira', '1978')
user2 = Usuarios('Taciana', 'Alencar', '1982')

print(Usuarios.nome_completo(user1))
print(Usuarios.nome_completo(user2))
print(Usuarios.idade(user2))