# Criar classe
class User:
  pass

# Criar objeto
user1 = User
user2 = User
# Criar parâmetros
user1.nome = 'Luciano'
user1.sobrenome = 'Pereira'
user1.nascimento = 1978
user2.nome = 'Taciana'
user2.sobrenome = 'Pereira'
user2.nascimento = 1982

# Print
print(f'Nome:{user1.nome}, Nascimento:{user1.nascimento}')
print(f'Nome:{user2.nome}, Nascimento:{user2.nascimento}')