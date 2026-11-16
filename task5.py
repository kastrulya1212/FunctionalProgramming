from functools import reduce

STUDENTS = [
	{"name": "Анна", "age":20, "grade":4.5},
    {"name": "Борис", "age":22, "grade":3.8},
    {"name": "Виктор", "age":19, "grade":4.2},
    {"name": "Галина", "age":21, "grade":4.9},
    {"name": "Дмитрий", "age":23, "grade":3.5}
]

# Уровень 1
#f1 = lambda elem: f'Имя: {elem["name"]}, Оценка: {elem["grade"]}'
GET_STRINGS = lambda students: tuple(
    map(
        lambda elem: f'Имя: {elem["name"]}, Оценка: {elem["grade"]}',
        students
    )
)

# ДЛЯ ТЕСТА
for i in GET_STRINGS(STUDENTS):
    print("Уровень 1: " + i)


# Уровень 2
GET_BEST_STUDENTS = lambda students: tuple(
    filter(
        lambda elem: elem["grade"] > 4.0,
        students
    )
)

# ДЛЯ ТЕСТА
for i in GET_BEST_STUDENTS(STUDENTS):
    print("Уровень 2: " + f'{i}')


# Уровень 3
GET_AVERAGE = lambda students: (
    reduce(
        lambda acc,x: acc+x, map(lambda elem: elem["age"], 
        students)
    ) / len(students)
)

# ДЛЯ ТЕСТА
print("Уровень 3: " + f'{GET_AVERAGE(STUDENTS)}')
