from typing import (
    SupportsInt,
    SupportsFloat,
    Collection,
)


def converter_bytes_para_megabytes(quantidade_bytes: SupportsInt) -> str:
    """Converte a quantidade de bytes para megabytes. Devolve uma string com até duas casas de precisão.

    >>> converter_bytes_para_megabytes(1048576)
    '1.00 MB'
    >>> converter_bytes_para_megabytes(20971520)
    '20.00 MB'
    >>> converter_bytes_para_megabytes(1000090)
    '0.95 MB'
    """
    try:
        quantidade_megabytes = int(quantidade_bytes) / (1024 * 1024)
        return f'{quantidade_megabytes:.2f} MB'
    except ValueError:
        raise ValueError('Valor não conversível para inteiro')


def obtem_valor_da_porcentagem(
    parcial: SupportsFloat, total: SupportsFloat
) -> str:
    """Obtem o valor da porcentagem, e retorna formatado como string em duas casas decimais
    >>> obtem_valor_da_porcentagem(5, 10)
    '50.00%'
    >>> obtem_valor_da_porcentagem(2, 4)
    '50.00%'
    >>> obtem_valor_da_porcentagem(8, 10)
    '80.00%'
    >>> obtem_valor_da_porcentagem(25, 10000)
    '0.25%'
    """
    try:
        return '{:.2%}'.format(float(parcial) / float(total))
    except ValueError:
        raise ValueError('Valor não conversível para float')


def calcular_media_total(
    valores: Collection[SupportsInt],
) -> tuple[float, int]:
    total = sum(valores)
    media = total / len(valores)

    return media, total
