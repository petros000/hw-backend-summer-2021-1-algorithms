__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    if not arr:
        return 0

    sum_even = 0
    sum_odd = 0

    for val in arr:
        if val % 2 == 0:
            sum_even += val
        else:
            sum_odd += val

    if sum_even == 0 or sum_odd == 0:
        return 0
    else:
        return sum_even/sum_odd


#print(even_odd([2, -1, 3]))
