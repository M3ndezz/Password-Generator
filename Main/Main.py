import random
import string
from Choice_of_password import Configs_Password


def gerar_senha(comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais):

    # Define os caracteres de acordo com a configuração escolhida
    # Armazenar os caracteres
    caracteres = ''

    if usar_maiusculas:
        # Acessa a biblioteca ascii e adiciona alfabeto na variavel (caracteres) em maiusculas
        caracteres += string.ascii_uppercase

    if usar_minusculas:
        # Acessa a biblioteca ascii e adiciona o alfabeto na variavel (caracteres) em minusculas
        caracteres += string.ascii_lowercase
    if usar_numeros:

        # Acessa a biblioteca ascii e adiciona numeros na variavel (caracteres)
        caracteres += string.digits

    if usar_especiais:
        # Acessa a biblioteca ascii e adiciona pontuações na variavel (caracteres)
        caracteres += string.punctuation

    # Garantir que pelo menos um tipo de caractere seja selecionado
    if not caracteres:
        raise ValueError("Nenhum tipo de caractere foi selecionado para a geração da senha.")

    # Gera a senha com uma String Vazia
    # Será juntada com o .join com a biblioteca random.choice que escolherá a posição
    # De cada Caractere armazenada no "caracteres" e começará um looping de uma variavel vazia "_"
    # Com o numero escolhido no comprimento
    criar_senha = "".join(random.choice(caracteres) for _ in range(comprimento))
    return criar_senha


# Teste
if __name__ == "__main__":
    print("O comprimento da senha deve ser maior que 5, para maior segurança!")
    comprimento_senha, usar_senha_maiusculas, usar_senha_minusculas, usar_senha_numeros, usar_senha_especiais =\
        Configs_Password.configs_password()
    senha = gerar_senha(comprimento_senha, usar_senha_maiusculas, usar_senha_minusculas, usar_senha_numeros,
                        usar_senha_especiais)

    print(f"Essa é a sua senha: {senha}")
