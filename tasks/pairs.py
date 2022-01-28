from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    out = []

    if arr1 and arr2:
        min_len = min(len(arr1), len(arr2))

        for i in range(min_len):
            out.append((arr1[i], arr2[i]))

    return out


#print(corresponding_pairs([1, 2, 5, 6], [3, 4]))
