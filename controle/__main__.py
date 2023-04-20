import typer
from rich.console import Console
from rich.table import Table

from controle.conversao import (
    converter_bytes_para_megabytes,
    obtem_valor_da_porcentagem,
    calcular_media_total,
)
from controle.leitor import ler_arquivo_usuarios

console = Console()
CAMINHO_ARQUIVO = 'archive/usuarios.txt'

def main(
    ordena: bool = typer.Option(
        False, '--ord', '-o', help='Ordena os usuários pelo espaço utilizado'
    )
):
    usuarios = ler_arquivo_usuarios(CAMINHO_ARQUIVO)
    if ordena:
        usuarios = sorted(
            usuarios,
            reverse=True,
            key=lambda usuario: usuario.espaco_utilizado,
        )

    table = Table(
        'Nr.', 'Usuário', 'Espaço utilizado', '% do uso', show_lines=True
    )

    media, total = calcular_media_total(
        [usuario.espaco_utilizado for usuario in usuarios]
    )
    for indice, usuario in enumerate(usuarios, start=1):
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


if __name__ == '__main__':
    typer.run(main)
