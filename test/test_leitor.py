from unittest import TestCase

from controle.leitor import ler_usuario
from controle.usuario import Usuario


class LeitorTest(TestCase):
    def test_devolve_dataclass_usuario(self):
        entrada = 'nome_usuario       22222222'
        saida_esperada = Usuario(nome='nome_usuario', espaco_utilizado=22222222)

        self.assertEqual(saida_esperada, ler_usuario(entrada))

    def test_deve_retornar_erro_ao_receber_mais_de_dois_parâmetros(self):
        entrada = 'nome_usuario       22222     outra_coisa'

        with self.assertRaisesRegex(ValueError, 'too many values to unpack'):
            ler_usuario(entrada)

    def test_deve_retornar_erro_ao_receber_menos_de_dois_parâmetros(self):
        entrada = 'nome_usuario  '

        with self.assertRaisesRegex(ValueError, 'not enough values to unpack'):
            ler_usuario(entrada)

