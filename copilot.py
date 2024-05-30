# Criação de uma lista vazia para armazenar os usuários
usuarios = []

while True:
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários cadastrados")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        # Solicita nome e sobrenome do usuário
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        
        # Verifica se ambos os campos foram preenchidos
        if nome and sobrenome:
            # Adiciona o usuário à lista
            usuarios.append((nome, sobrenome))
            print("Usuário cadastrado com sucesso!")
        else:
            print("Por favor, preencha todos os campos.")
    elif opcao == "2":
        # Lista os usuários cadastrados
        print("\nUsuários cadastrados:")
        for usuario in usuarios:
            print(f"{usuario[0]} {usuario[1]}")
    elif opcao == "3":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")