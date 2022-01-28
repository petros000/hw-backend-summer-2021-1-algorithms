from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    words = text.split()
    print(words)
    res = (None, None)

    if len(words) > 1:
        min_word = words[0]
        max_word = words[1]
        for w in words:
            if len(w) < len(min_word):
                min_word = w
            if len(w) > len(max_word):
                max_word = w
        res = (min_word, max_word)

    return res


print(find_shortest_longest_word('hello there, general kenobi'))
