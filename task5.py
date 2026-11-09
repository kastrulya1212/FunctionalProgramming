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
# strings = map(
#     lambda elem: f'Имя: {elem["name"]}, Оценка: {elem["grade"]}',
#     STUDENTS
# )
def get_strings(students: list[dict]):
    return map(
        lambda elem: f'Имя: {elem["name"]}, Оценка: {elem["grade"]}',
        students
    )

print(list(get_strings(STUDENTS)))

# Уровень 2
# best_students = filter(
#     lambda elem: elem["grade"] > 4,
#     STUDENTS
# )
def get_best_students(students: list[dict]):
    return filter(
        lambda elem: elem["grade"] > 4,
        students
    )

print(list(get_best_students(STUDENTS)))

# Уровень 3
# sum = reduce(lambda acc,x: acc+x, map(lambda elem: elem["age"], STUDENTS))
# avg_age = sum / len(STUDENTS)
def average_age(students: list[dict]):
    return reduce(lambda acc,x: acc+x, map(lambda elem: elem["age"], students)) / len(students)

print(average_age(STUDENTS))