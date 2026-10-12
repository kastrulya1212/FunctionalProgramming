import enum
from dataclasses import dataclass
from typing import Generic, TypeVar, Union

# Уровень 1
# Создали тип-сумму с вариантами LOADING, SUCCESS, ERROR
class LoadState(enum.Enum):
    LOADING = 100
    SUCCESS = 200
    ERROR = 500

# Уровень 2
# Создали тип-произведение с полями name, age, email
@dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str

# Уровень 3 
# Создали тип-сумму success и failure и далее функцию load_users
# В задании параметры функции пустые, но решил добавить список users иначе
# неоткуда брать входные данные
T = TypeVar("T")
E = TypeVar("E")

@dataclass(frozen=True)
class Success(Generic[T]):
    value: T

@dataclass(frozen=True)
class Failure(Generic[E]):
    value: E

Result = Union[Success[T], Failure[E]]

def load_users(users: list[User]) -> Result[list[User], str]:
    return Success(users) if users else Failure("Пустой список!")