from pprint import pprint as print
from contextlib import redirect_stdout

from controle.conversao import converter_bytes_para_megabytes
from controle.leitor import ler_usuario

with open('arquivos/usuarios.txt', mode='r') as file:
    usuarios = [ler_usuario(linha) for linha in file.readlines() if linha is not '\n']

total = sum(usuario.espaco_utilizado for usuario in usuarios)

cabecalho = ('Nr.', 'Usuário', 'Espaço utilizado', '% do uso')
linhas = [cabecalho]

for (index, usuario) in enumerate(usuarios, start=1):
    porcentagem = '{:.2%}'.format((usuario.espaco_utilizado / total))
    espaco_utilizado_megabytes = f'{converter_bytes_para_megabytes(usuario.espaco_utilizado):.2f} MB'

    linhas.append((index, usuario.nome, espaco_utilizado_megabytes, porcentagem))


STRING_FORMATACAO = '{:<5}{:<20}{:>20}{:>20}' 
with (open('arquivos/relatorio.txt', mode='w', encoding='utf-8')) as file:
    linhasParaEscrever = [
        'ACME Inc.           Uso do espaço em disco pelos usuários',
        '-' * 65,
        *[STRING_FORMATACAO.format(*l) for l in linhas],
        'Espaço total ocupado: {} MB'.format(converter_bytes_para_megabytes(total)),
        'Espaço médio ocupado: {:.2f} MB'.format(converter_bytes_para_megabytes(total) / len(usuarios))
    ]

    linhasParaEscrever = [f'{linha}\n' for linha in linhasParaEscrever]

    file.writelines(linhasParaEscrever)