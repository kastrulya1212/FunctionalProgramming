from functools import partial


# Уровень 1
# Каррированная функция, которая возвращает список элементов у которых 
# item[key] == value 
filter_by = lambda key: lambda value: lambda items: list(
    filter(lambda item: item[key] == value, items)
)


# Уровень 2
# Функция, которая заранее задает key = "category" для функции filter_by
filter_by_category = partial(
    lambda key, value, items: filter_by(key)(value)(items),
    "category"
)


# Уровень 3
# Тоже каррированная функция, которая сообщает x > threshold
greater_than = lambda threshold: lambda x: x > threshold

# Пример применения с filter (из списка чисел выбирает те, которые больше указанного в параметре функции)
# list(filter(greater_than(5), [1, 6, 8, 2, 9]))