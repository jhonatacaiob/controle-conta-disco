from unittest import TestCase

from controle.conversao import (
    converter_bytes_para_megabytes,
    obtem_valor_da_porcentagem,
)


class ConversaoBytesMegabytesTest(TestCase):
    def test_realiza_conversao(self):
        entrada = 1024 * 1024
        saida_esperada = '1.00 MB'
        self.assertEqual(
            saida_esperada, converter_bytes_para_megabytes(entrada)
        )

    def test_deve_realizar_conversao_ao_passar_um_float(self):
        entrada = 1024.0 * 1024
        saida_esperada = '1.00 MB'
        self.assertEqual(
            saida_esperada, converter_bytes_para_megabytes(entrada)
        )

    def test_deve_realizar_conversao_ao_passar_uma_string_conversivel(self):
        entrada = 2 * 1024 * 1024
        saida_esperada = '2.00 MB'
        self.assertEqual(
            saida_esperada, converter_bytes_para_megabytes(str(entrada))
        )

    def test_deve_realizar_conversao_e_retornar_um_valor_arredondado(self):
        entrada = 786432
        saida_esperada = '0.75 MB'
        self.assertEqual(
            saida_esperada, converter_bytes_para_megabytes(entrada)
        )

    def test_deve_retornar_um_erro_ao_passar_um_valor_não_conversivel(self):
        entrada = 'uma_string'

        with self.assertRaisesRegex(
            ValueError, 'Valor não conversível para inteiro'
        ):
            converter_bytes_para_megabytes(entrada)

class ValorDaPorcentagemTest(TestCase):
    def test_aplica_porcentagem(self):
        entrada = (2, 4)
        saida_esperada = '50.00%'
        self.assertEqual(
            saida_esperada, obtem_valor_da_porcentagem(*entrada)
        )

    def test_deve_aplicar_porcentagem_quando_primeiro_for_conversivel(
        self,
    ):
        entrada = ('2.0', 4)
        saida_esperada = '50.00%'
        self.assertEqual(
            saida_esperada, obtem_valor_da_porcentagem(*entrada)
        )

    def test_deve_aplicar_porcentagem_quando_segundo_for_conversivel(self):
        entrada = (3, '12.0')
        saida_esperada = '25.00%'
        self.assertEqual(
            saida_esperada, obtem_valor_da_porcentagem(*entrada)
        )

    def test_deve_retornar_erro_quando_algum_valor_não_for_conversivel(self):
        entradas = [
            (3, 'porta'),
            ('maca', 4),
            ('uma_string', 'duas_string'),
        ]

        for primeiro, segundo in entradas:
            with self.subTest(
                primeiro=primeiro, segundo=segundo
            ), self.assertRaisesRegex(
                ValueError, 'Valor não conversível para float'
            ):
                obtem_valor_da_porcentagem(primeiro, segundo)
