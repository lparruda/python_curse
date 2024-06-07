'''
Functions (Funções)

DRY - Don't Repeat Yourself.

'''
def finput(msg):
    while True:
       entrada = input(msg)
       if entrada.strip():
            return entrada
       else:
         print("Erro! Digite conforme solicitado.")

# def f_input(mensagem):
#     while True:
#         entrada = input(mensagem)
#         if entrada.strip():
#             return entrada
#         else:
#             print('Erro! Digite conforme solicitado.')


nome = finput("Digite seu nome:")
sobrenome = finput("Digite seu sobrenome:")
resposta = f"Cadastro realizado. Seu nome é {nome} e seu sobrenome é {sobrenome}"
print(resposta)