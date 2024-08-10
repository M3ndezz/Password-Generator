def configs_password():
    comprimento = int(input("Digite o comprimento da senha: "))
    if not comprimento >= 5:
        raise ValueError("escolha o comprimento maior que 5, para senha mais segura!")
    usar_maiusculas = input("Deseja incluir letras maiúsculas? (s/n) ").lower() == 's'
    usar_minusculas = input("Deseja incluir letras minúsculas? (s/n) ").lower() == 's'
    usar_numeros = input("Deseja incluir números? (s/n) ").lower() == 's'
    usar_especiais = input("Deseja incluir caracteres especiais? (s/n) ").lower() == 's'

    return comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais
