import random
import string


def gerar_senha(comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais):
    """Gera uma senha aleatória com o comprimento e tipos de caracteres especificados.

    Args:
        comprimento (int): O comprimento da senha a ser gerada.
        usar_maiusculas (bool): Incluir letras maiúsculas. A escolha do usuário.

        usar_minusculas (bool): Incluir letras minúsculas. A escolha do usuário.

        usar_numeros (bool): Incluir números. A escolha do usuário.

        usar_especiais (bool): Incluir caracteres especiais. A escolha do usuário.

    Returns:
        str: Uma senha gerada aleatoriamente.
    """
    # Define os conjuntos de caracteres disponíveis
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation

    # Garantir que pelo menos um tipo de caractere seja selecionado
    if not caracteres:
        raise ValueError("Nenhum tipo de caractere foi selecionado para a geração da senha.")

    # Gera a senha
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha


# Exemplo de uso
if __name__ == "__main__":
    comprimento = int(input("Digite o comprimento da senha: "))
    usar_maiusculas = input("Deseja incluir letras maiúsculas? (s/n) ").lower() == 's'
    if usar_maiusculas == "s":
        usar_maiusculas = True
    usar_minusculas = input("Deseja incluir letras minúsculas? (s/n) ").lower() == 's'
    if usar_maiusculas == "s":
        usar_minusculas = True
    usar_numeros = input("Deseja incluir números? (s/n) ").lower() == 's'
    if usar_numeros == "s":
        usar_numeros = True
    usar_especiais = input("Deseja incluir caracteres especiais? (s/n) ").lower() == 's'
    if usar_especiais == "s":
        usar_especiais = True
    senha = gerar_senha(comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais)
    print(f"Essa é a sua senha: {senha}")
