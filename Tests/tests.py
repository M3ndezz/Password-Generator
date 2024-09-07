import unittest
import string

from Main.Main import gerar_senha


class TestGeradorDeSenha(unittest.TestCase):

    def test_comprimento_senha(self):
        senha = gerar_senha(10, True, True, True, True)
        self.assertEqual(len(senha), 10)

    def test_uso_de_maiusculas(self):
        senha = gerar_senha(10, True, False, False, False)
        self.assertTrue(any(c.isupper() for c in senha))

    def test_uso_de_minusculas(self):
        senha = gerar_senha(10, False, True, False, False)
        self.assertTrue(any(c.islower() for c in senha))

    def test_uso_de_numeros(self):
        senha = gerar_senha(10, False, False, True, False)
        self.assertTrue(any(c.isdigit() for c in senha))

    def test_uso_de_especiais(self):
        senha = gerar_senha(10, False, False, False, True)
        self.assertTrue(any(c in string.punctuation for c in senha))


if __name__ == "__main__":
    unittest.main()
