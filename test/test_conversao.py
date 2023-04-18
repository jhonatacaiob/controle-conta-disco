from unittest import TestCase

from controle.conversao import converter_bytes_para_megabytes


class ConversaoTest(TestCase):
    def test_realiza_conversao(self):
        entrada = 1024 * 1024
        self.assertEqual(1, converter_bytes_para_megabytes(entrada))

    def test_deve_realizar_conversao_ao_passar_um_float(self):
        entrada=1024.0 * 1024
        self.assertEqual(1, converter_bytes_para_megabytes(entrada))

    def test_deve_realizar_conversao_ao_passar_uma_string_conversivel(self):
        entrada=2 * 1024 * 1024
        self.assertEqual(2, converter_bytes_para_megabytes(str(entrada)))
        
    def test_deve_realizar_conversao_e_retornar_um_valor_arredondado(self):
        entrada=786432
        self.assertEqual(0.75, converter_bytes_para_megabytes(entrada))

    def test_deve_retornar_um_erro_ao_passar_um_valor_não_conversivel(self):
        entrada='uma_string'

        with self.assertRaisesRegex(ValueError, 'Valor não conversível para inteiro'):
            converter_bytes_para_megabytes(entrada)
        