import csv
import io
from typing import Optional


# Уровень 1
# Преобразовывем CSV-строку в список словарей пропуская пустые строки
def parse_csv(data: str) -> list[dict]:
    return list(csv.DictReader(io.StringIO(data)))


# Уровень 2
# Вычисляем сумму quantity * price для всех строк
def compute_revenue(rows: list[dict]) -> float:
    return sum(float(row["quantity"]) * float(row["price"]) for row in rows)


# Уровень 3
# Находим строку с максимальной выручкой или возвращаем None для пустого списка
def top_item(rows: list[dict]) -> Optional[dict]:
    if len(rows) == 0:
        return None
    return max(
        rows,
        key=lambda row: float(row["quantity"]) * float(row["price"])
    )



# ------------ tests ------------
# def run_tests() -> None:
#     data = """id,category,name,date,price,quantity
# 1,Электротехника,Телевизор,2021-05-15,15000,3
# 2,Электротехника,Холодильник,2021-06-20,25000,2
# """
#     print(parse_csv(data))
#     print(compute_revenue(parse_csv(data)))
#     print(top_item(parse_csv(data)))
# run_tests()