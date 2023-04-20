from unittest import TestCase
from unittest.mock import patch, mock_open

from controle.leitor import ler_usuario, ler_arquivo_usuarios
from controle.usuario import Usuario


class LeitorTest(TestCase):
    def test_devolve_dataclass_usuario(self):
        entrada = 'nome_usuario       22222222'
        saida_esperada = Usuario(
            nome='nome_usuario', espaco_utilizado=22222222
        )

        self.assertEqual(saida_esperada, ler_usuario(entrada))

    def test_deve_retornar_erro_ao_receber_mais_de_dois_parâmetros(self):
        entrada = 'nome_usuario       22222     outra_coisa'

        with self.assertRaisesRegex(ValueError, 'too many values to unpack'):
            ler_usuario(entrada)

    def test_deve_retornar_erro_ao_receber_menos_de_dois_parâmetros(self):
        entrada = 'nome_usuario  '

        with self.assertRaisesRegex(ValueError, 'not enough values to unpack'):
            ler_usuario(entrada)

    @patch('builtins.open', new_callable=mock_open, read_data='teste   2')
    def test_deve_chamar_o_open_com_a_string_passada_como_argumento(
        self, mock_file
    ):
        path = 'arquivos/abluble.txt'
        ler_arquivo_usuarios(path)
        mock_file.assert_called_with(path, mode='r')

    def test_deve_dar_erro_caso_arquivo_não_existe(self):
        with self.assertRaisesRegex(
            FileNotFoundError, 'Arquivo informado não existe'
        ):
            ler_arquivo_usuarios('arquivos/abluble.txt')

    @patch(
        'builtins.open',
        new_callable=mock_open,
        read_data='\n'.join(
            [
                'usuario1          1',
                'usuario2          2',
                'usuario3          3',
                'usuario4          4',
                'usuario5          5',
                'usuario6          6',
                'usuario7          7',
                'usuario8          8',
                'usuario9          9',
            ]
        ),
    )
    def test_retorna_lista_com_usuarios(self, mock_file):
        saida_esperada = [
            Usuario(nome='usuario1', espaco_utilizado=1),
            Usuario(nome='usuario2', espaco_utilizado=2),
            Usuario(nome='usuario3', espaco_utilizado=3),
            Usuario(nome='usuario4', espaco_utilizado=4),
            Usuario(nome='usuario5', espaco_utilizado=5),
            Usuario(nome='usuario6', espaco_utilizado=6),
            Usuario(nome='usuario7', espaco_utilizado=7),
            Usuario(nome='usuario8', espaco_utilizado=8),
            Usuario(nome='usuario9', espaco_utilizado=9),
        ]
        saida = ler_arquivo_usuarios('arquivos/abluble.txt')
        self.assertEqual(saida_esperada, saida)
