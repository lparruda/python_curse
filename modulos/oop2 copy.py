class Usuarios:
    pass
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

user1 = Usuarios('Luciano', 'Pereira', '1978')
user2 = Usuarios('Taciana', 'Alencar', '1982')
print(user1.nome)
print(user2.nome)
print(user1.nome_completo())