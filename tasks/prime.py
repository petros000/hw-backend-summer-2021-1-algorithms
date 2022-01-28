__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number <= 1:
        return False

    for num in range(2, number + 1):
        if number % num == 0 and number != num:
            return False
    return True


