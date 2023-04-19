from controle.conversao import (
    converter_bytes_para_megabytes,
    obtem_valor_da_porcentagem,
)
from controle.leitor import ler_usuario

with open('archive/usuarios.txt', mode='r') as file:
    usuarios = [ler_usuario(linha) for linha in file.readlines() if linha != '\n']

total = sum(usuario.espaco_utilizado for usuario in usuarios)

cabecalho = ('Nr.', 'Usuário', 'Espaço utilizado', '% do uso')
linhas = [cabecalho]

for index, usuario in enumerate(usuarios, start=1):
    porcentagem = obtem_valor_da_porcentagem(usuario.espaco_utilizado, total)
    espaco_utilizado_megabytes = converter_bytes_para_megabytes(
        usuario.espaco_utilizado
    )

    linhas.append((index, usuario.nome, espaco_utilizado_megabytes, porcentagem))


STRING_FORMATACAO = '{:<5}{:<20}{:>20}{:>20}'
with open('archive/relatorio.txt', mode='w', encoding='utf-8') as file:
    linhasParaEscrever = [
        'ACME Inc.           Uso do espaço em disco pelos usuários',
        '-' * 65,
        *[STRING_FORMATACAO.format(*l) for l in linhas],
        f'Espaço total ocupado: {converter_bytes_para_megabytes(total)}',
        f'Espaço médio ocupado: {converter_bytes_para_megabytes(total / len(usuarios))}',
    ]

    linhasParaEscrever = [f'{linha}\n' for linha in linhasParaEscrever]

    file.writelines(linhasParaEscrever)
