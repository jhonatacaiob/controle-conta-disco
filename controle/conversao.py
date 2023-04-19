from typing import (
    SupportsInt,
    SupportsFloat,
)


def converter_bytes_para_megabytes(quantidade_bytes: SupportsInt) -> float:
    """Converte a quantidade de bytes para megabytes. Com até duas casas de precisão.

    >>> converter_bytes_para_megabytes(1048576)
    1.0
    >>> converter_bytes_para_megabytes(20971520)
    20.0
    >>> converter_bytes_para_megabytes(1000090)
    0.95
    """
    try:
        quantidade_mega = int(quantidade_bytes) / (1024 * 1024)
        return round(quantidade_mega, 2)
    except ValueError:
        raise ValueError('Valor não conversível para inteiro')


def obtem_valor_da_porcentagem(parcial: SupportsFloat, total: SupportsFloat) -> str:
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
        raise ValueError("Valor não conversível para float")
