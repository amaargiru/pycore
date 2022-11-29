# Утиная типизация (duck types) - постулирование реализации интерфейса классом не через явное объявление, а через реализацию методов
# интерфейса. Так, каждый класс, реализующий методы next() и iter(), автоматически становится итератором, несмотря на отсутствие явного
# объявления (что-нибудь вроде @iterator) или, скажем, наследования от класса Iterator.
from functools import total_ordering


# Iterator
# Итератор - класс, реализующий методы next() и iter().
# Метод next() должен возвращать следующее значение итератора или выкидывать исключение StopIteration, чтобы сигнализировать о том,
# что итератор исчерпал доступные значения.
# Метод iter() должен возвращать "self".

class LimitCounter:
    def __init__(self, max_value: int):
        self.count = 0
        self.max_value = max_value

    def __next__(self):
        self.count += 1

        if self.count <= self.max_value:
            return self.count
        else:
            raise StopIteration

    def __iter__(self):
        return self


limit_counter = LimitCounter(2)
print(next(limit_counter))
print(next(limit_counter))


# print(next(limit_counter))  # Raises StopIteration

# Comparable
# Начиная с Python 3.4, для того, чтобы экземпляры метода можно было сравнивать между собой, достаточно определить методы lt (меньше)
# и eq (равно), а также задействовать декоратор @functools.total_ordering.

@total_ordering
class Person:
    def __init__(self, firstname: str, lastname: str):
        self.firstname: str = firstname
        self.lastname: str = lastname

    def _is_valid_operand(self, other):
        return hasattr(other, "lastname") and hasattr(other, "firstname")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.lastname, self.firstname) == (other.lastname, other.firstname)

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.lastname, self.firstname) < (other.lastname, other.firstname)


Finn = Person("Finn", "the Human")
Jake = Person("Jake", "the Dog")

print(Finn != Jake)


# Hashable
# Хешируемые объекты должны реализовывать методы hash() и eq(). Хеш объекта должен быть неизменен в течении всего жизненного цикла.
# Хешируемые объекты можно использовать как ключи в словарях и как элементы множеств, так как эти структуры используют хеш-таблицу
# для внутреннего представления данных.


class Hero:
    def __init__(self, name: str, level: int):
        self.name: str = name
        self.level: int = level

    def _is_valid_operand(self, other):
        return hasattr(other, "name") and hasattr(other, "level")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.name, self.level) == (other.name, other.level)

    def __hash__(self):
        return hash((self.name, self.level))


Finn = Hero("Finn the Human", 10_000)
Jake = Hero("Jake the Dog", 10_000)

print(hash(Finn))
print(hash(Jake))

# Sortable
# Для возможности применения к последовательностям объектов таких методов как sort() или max() необходимо, как и в случае Comparable,
# определить методы lt (меньше) и eq (равно), а также задействовать декоратор @functools.total_ordering.

# Для примера создадим класс студентов, которых можно будет сортировать не по имени, а по среднему баллу.
from statistics import mean


@total_ordering
class Student:
    def __init__(self, name: str, grades: list[int]):
        self.name: str = name
        self.grades: list[int] = grades

    def _is_valid_operand(self, other):
        return hasattr(other, "name") and hasattr(other, "grades")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return mean(self.grades) == mean(other.grades)

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return mean(self.grades) < mean(other.grades)

    # str определим просто для нормальной человеко-читаемой репрезентации объекта.
    def __str__(self):
        return self.name + " " + str(mean(self.grades))


Melissa = Student("Melissa Andrew", [4, 3, 4, 5, 4])
Peter = Student("Peter Shining Jr.", [3, 3, 4, 5, 3])
Joe = Student("Just Joe", [5, 5, 4, 5, 5])

print([str(stud) for stud in sorted([Peter, Melissa, Joe], reverse=True)])
