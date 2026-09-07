import csv
import io
from typing import Optional


# Уровень 1
def parseCsv(data: str) -> list[dict]:
    return list(csv.DictReader(io.StringIO(data)))

# Уровень 2
def computeRevenue(rows: list[dict]) -> float:
    return sum(float(row['price']) * int(row['count']) for row in rows)

# Уровень 3
def topItem(rows: list[dict]) -> Optional[dict]:
    if len(rows) == 0:
        return None
    
    max_row = rows[0]
    for row in rows:
        if computeRevenue([row]) > computeRevenue([max_row]):
            max_row = row
    return max_row


# Тесты
def globalTest():
    data = """id,category,name,date,price,count
        1, Электротехника, Телевизор, 2021-05-15, 15000, 3
        2, Электротехника, Холодильник, 2021-06-20, 25000, 2"""
    empty_data = """id,category,name,date,price,count"""


    print("ТЕСТЫ С ПОЛНЫМИ ДАННЫМИ")
    print("Уровень 1 тест:")
    parsed_data = parseCsv(data)
    for item in parsed_data:
        print(item)


    print("\nУровень 2 тест:")
    revenue = computeRevenue(parsed_data)
    print(f"Общий доход: {revenue}")


    print("\nУровень 3 тест:")
    top = topItem(parsed_data)
    print(f"Товар с наибольшим доходом: {top}")



    print("\n\nТЕСТЫ С ПУТСЫМИ ДАННЫМИ")
    print("Уровень 1 тест:")
    parsed_data = parseCsv(empty_data)
    for item in parsed_data:
        print(item)


    print("\nУровень 2 тест:")
    revenue = computeRevenue(parsed_data)
    print(f"Общий доход: {revenue}")


    print("\nУровень 3 тест:")
    top = topItem(parsed_data)
    print(f"Товар с наибольшим доходом: {top}")



globalTest()