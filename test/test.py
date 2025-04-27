import unittest
from src.main import criar_personagem

class TesteCriarPersonagem(unittest.TestCase):

    def teste_criar_personagem_valido(self):
        personagem = criar_personagem("tino soldado", 76, "soldado", 67, "soco forte")
        self.assertEqual(personagem["Nome"], "tino soldado")
        self.assertEqual(personagem["Idade"], 76)
        self.assertEqual(personagem["Tipo"], "soldado")
        self.assertEqual(personagem["Força"], 67)
        self.assertEqual(personagem["Habilidade Especial"], "soco forte")

    def teste_idade_invalida(self):
        with self.assertRaises(ValueError):
            criar_personagem("tino soldado", 9, "soldado", 67, "soco forte")

    def teste_forca_invalida(self):
        with self.assertRaises(ValueError):
            criar_personagem("tino soldado", 76, "soldado", 150, "soco forte")

    def teste_nome_vazio(self):
        with self.assertRaises(ValueError):
            criar_personagem("", 76, "soldado", 67, "soco forte")

    def teste_tipo_invalido(self):
        with self.assertRaises(ValueError):
            criar_personagem("tino soldado", 76, "", 67, "soco forte")

if __name__ == "__main__":
    unittest.main()
