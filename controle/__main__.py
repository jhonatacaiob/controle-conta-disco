import typer
from rich.console import Console
from rich.table import Table

from controle.conversao import (
    converter_bytes_para_megabytes,
    obtem_valor_da_porcentagem,
    calcular_media_total,
)
from controle.leitor import ler_arquivo_usuarios
from controle.usuario import Usuario

console = Console()
CAMINHO_ARQUIVO = 'archive/usuarios.txt'


def monta_table_e_exibe(
    lista_usuarios: list[Usuario], numero_linhas: int | None
):
    table = Table(
        'Nr.', 'Usuário', 'Espaço utilizado', '% do uso', show_lines=True
    )

    media, total = calcular_media_total(
        [usuario.espaco_utilizado for usuario in lista_usuarios]
    )

    if numero_linhas:
        lista_usuarios = lista_usuarios[:numero_linhas]

    for indice, usuario in enumerate(lista_usuarios, start=1):
        table.add_row(
            str(indice),
            usuario.nome,
            converter_bytes_para_megabytes(usuario.espaco_utilizado),
            obtem_valor_da_porcentagem(usuario.espaco_utilizado, total),
        )

    table.add_row(
        '', 'Espaço total ocupado', converter_bytes_para_megabytes(total)
    )
    table.add_row(
        '', 'Espaço médio ocupado', converter_bytes_para_megabytes(media)
    )

    console.print(table)


def main(
    ordena: bool = typer.Option(
        False, '--ord', '-o', help='Ordena os usuários pelo espaço utilizado'
    ),
    numero_linhas: int = typer.Option(
        None,
        '--numero-linhas',
        '-n',
        help='Apresenta os n primeiros da lista',
        show_default=False,
    ),
):
    usuarios = ler_arquivo_usuarios(CAMINHO_ARQUIVO)
    if ordena:
        usuarios = sorted(
            usuarios,
            reverse=True,
            key=lambda usuario: usuario.espaco_utilizado,
        )

    monta_table_e_exibe(usuarios, numero_linhas)


if __name__ == '__main__':
    typer.run(main)
