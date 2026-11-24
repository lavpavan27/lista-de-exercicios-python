senha_correta = "Admin123"
tentativas = 0
 
while tentativas < 3:
    senha = input("Digite a senha: ")
 
    if senha == senha_correta:
        print("Login efetuado")
        break
    else:
        tentativas += 1
        if tentativas == 3:
    print("Conta bloqueada")