import re
import collections
from typing import Optional

# Уровень 1
# Ищем в строке слова, приводим все к нижнему реестру
# Для поиска использует регулярное выражение/шаблон r'[\w_]+', 
# [] один из; \w буква цифра или подчеркивание; + один или более раз
def split_words(text: str) -> list[str]:
    return re.findall(r'[\w_]+', text.lower())

# Уровень 2
# Считаем количество вхождений каждого слова в списке и
# возвращенный объект Counter преобразуем в словарь
def count_word_frequencies(words: list[str]) -> dict[str, int]:
    return dict(collections.Counter(words))

# Уровень 3
# Находим слово с максимальной частотой или возвращаем None для пустого словаря
def top_word(freq: dict[str, int]) -> Optional[str]:
    return max(
        freq.keys(),
        key=freq.get
    ) if freq else None





# # ------------ tests ------------
# print(split_words("Hello, world! 123"))
# print(count_word_frequencies(["hello", "world", "hello", "world", "world"]))
# print(top_word({"hello": 2, "world": 3}))
# 
# print(split_words(""))
# print(count_word_frequencies([]))
# print(top_word({}))