import random
import string


def gerar_senha(comprimento, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_especiais=True):
    """Gera uma senha aleatória com o comprimento e tipos de caracteres especificados.

    Args:
        comprimento (int): O comprimento da senha a ser gerada.
        usar_maiusculas (bool): Incluir letras maiúsculas. Padrão é True.
        usar_minusculas (bool): Incluir letras minúsculas. Padrão é True.
        usar_numeros (bool): Incluir números. Padrão é True.
        usar_especiais (bool): Incluir caracteres especiais. Padrão é True.

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
    comprimento = 12
    senha = gerar_senha(comprimento)
    print(f"Senha gerada: {senha}")
