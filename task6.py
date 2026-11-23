from dataclasses import dataclass
from typing import Generic, TypeVar, Callable



T = TypeVar("T")
U = TypeVar("U")


ORDERS = (
    {"id": 1, "total": 1500.0, "status": "paid"},
    {"id": 2, "total": 2300.0, "status": "pending"},
    {"id": 3, "total": 1000.0, "status": "cancelled"}
)


# Уровень 1 
# Извлекаем список сумм заказов при помощи map
GET_TOTALS = lambda orders: map(
    lambda order: order["total"],
    orders
)


# Уровень 2
# Создали тип обертку, который может содержать значение типа T или None. 
# Также добавили метод map, который применяет функцию к значению внутри OptionalBox, если оно не None
@dataclass(frozen=True)
class OptionalBox(Generic[T]):
    value: T | None

    def map(self, func: Callable[[T], U]) -> "OptionalBox[U]":
        return (
            OptionalBox(func(self.value))
            if self.value is not None
            else OptionalBox(None)
        )

# Уровень 3
# Безопасно извлекаем заказ по его идентификатору, возвращая OptionalBox с найденным заказом или None, если заказ не найден
GET_ORDER_BY_ID = lambda orders: lambda order_id: OptionalBox(
    next(
        filter(
            lambda order: order["id"] == order_id,
            orders
        ),
        None
    )
)


### ТЕСТЫ
# Тест уровня 1
print(GET_TOTALS(ORDERS))


# Тест уровня 3 - заказ существует
print(
    GET_ORDER_BY_ID(ORDERS)(2)
)


# Тест уровня 3 - заказа нет
print(
    GET_ORDER_BY_ID(ORDERS)(100)
)