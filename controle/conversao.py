from typing import SupportsInt

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