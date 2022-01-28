__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    convert_dict = {'d': 24*60*60, 'h': 1*60*60, 'm': 1*60, 's': 1}

    if seconds == 0:
        return '00s'

    out = ''

    for key, val in convert_dict.items():
        integer_division = seconds // val
        seconds %= val
        if integer_division != 0 or out != '':
            out += ('{:02}'.format(integer_division) + key)

    return out





