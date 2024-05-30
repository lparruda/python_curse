def cadastro_usuario():
  while True:
    nome = input("Digite seu nome: ")
    if nome.strip():
      break
    else:
      print("Erro! Digite seu nome.")
  while True:
    sobrenome = input("Digite seu sobrenome: ")
    if sobrenome.strip():
      break
    else:
      print("Erro! Digite seu sobrenome.")
  return {"nome": nome, "sobrenome": sobrenome}

def main():
  usuario = cadastro_usuario()
  print(f"\nUsuário cadastrado com sucesso!")
  print(f"Nome: {usuario['nome']}")
  print(f"Sobrenome: {usuario['sobrenome']}")
if __name__ == "__main__":
  main()
