import typer
from rich.console import Console
from rich.table import Column, Table

from controle.conversao import (
    converter_bytes_para_megabytes,
    obtem_valor_da_porcentagem,
)
from controle.leitor import ler_usuario

console = Console()


def main():
    table = Table('Nr.', 'Usuário', 'Espaço utilizado', '% do uso', show_lines=True)

    with open('archive/usuarios.txt', mode='r') as file:
        usuarios = [ler_usuario(linha) for linha in file.readlines() if linha != '\n']
        total = sum(usuario.espaco_utilizado for usuario in usuarios)
        media = sum(usuario.espaco_utilizado for usuario in usuarios) / len(usuarios)

        for indice, usuario in enumerate(usuarios, start=1):
            table.add_row(
                str(indice),
                usuario.nome,
                converter_bytes_para_megabytes(usuario.espaco_utilizado),
                obtem_valor_da_porcentagem(usuario.espaco_utilizado, total),
            )

    table.add_row('Espaço total ocupado', converter_bytes_para_megabytes(total))
    table.add_row('Espaço médio ocupado', converter_bytes_para_megabytes(media))

    console.print(table)


if __name__ == "__main__":
    typer.run(main)