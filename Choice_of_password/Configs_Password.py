def configs_password():
    comprimento_senha = int(input("Digite o comprimento da senha: "))
    if not comprimento_senha >= 5:
        raise ValueError("escolha o comprimento maior que 5, para senha mais segura!")
    usar_senha_maiusculas = input("Deseja incluir letras maiúsculas? (s/n) ").lower() == 's'
    usar_senha_minusculas = input("Deseja incluir letras minúsculas? (s/n) ").lower() == 's'
    usar_senha_numeros = input("Deseja incluir números? (s/n) ").lower() == 's'
    usar_senha_especiais = input("Deseja incluir caracteres especiais? (s/n) ").lower() == 's'

    return comprimento_senha, usar_senha_maiusculas, usar_senha_minusculas, usar_senha_numeros, usar_senha_especiais
