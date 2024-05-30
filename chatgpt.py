def cadastrar_usuario():
    while True:
        nome = input("Digite o nome: ").strip()
        if nome:
            break
        else:
            print("Nome não pode ser vazio. Por favor, digite novamente.")
    
    while True:
        sobrenome = input("Digite o sobrenome: ").strip()
        if sobrenome:
            break
        else:
            print("Sobrenome não pode ser vazio. Por favor, digite novamente.")
    
    print(f"Usuário cadastrado com sucesso: {nome} {sobrenome}")

if __name__ == "__main__":
 cadastrar_usuario()
