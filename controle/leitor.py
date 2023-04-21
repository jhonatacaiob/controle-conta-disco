from os import PathLike

from controle.usuario import Usuario


def ler_usuario(linha_arquivo: str) -> Usuario:
    """
    Lê a linha do arquivo e devolve um objeto do tipo Usuario.

    Contendo os nome do usuário, e o espaço utilizado pelo usuário

    >>> ler_usuario('nome_usuario       22222222')
    Usuario(nome='nome_usuario', espaco_utilizado=22222222)

    >>> ler_usuario('nome_usuario       22222222')
    Usuario(nome='nome_usuario', espaco_utilizado=22222222)
    """
    try:
        [nome_usuario, espaco_utilizado] = linha_arquivo.split()
        return Usuario(
            nome=nome_usuario, espaco_utilizado=int(espaco_utilizado)
        )

    except ValueError as err:
        raise ValueError(
            f'Erro nos parâmetros fornecidos, o seguinte erro ocorreu: {err}'
        )


def ler_arquivo_usuarios(caminho: str | bytes | PathLike) -> list[Usuario]:
    try:
        with open(caminho, mode='r') as file:
            usuarios = [ler_usuario(linha) for linha in file if linha != '\n']
            return usuarios
    except:
        raise FileNotFoundError('Arquivo informado não existe')
