# Специальные (называемые также magic или dunder) методы класса - перегрузка, позволяющая классам определять собственное поведение
# по отношению к операторам языка.
import math

print(dir(int))


class A:  # An empty class
    ...


a = A()
print(dir(a))
print(repr(a))
print(str(a))


# Особенностью метода __init__ является то, что он не должен ничего возвращать. При попытке возврата данных будет сгенерировано
# исключение.
# __repr__ (representation) возвращает более-менее машино-читаемое представление объекта, полезное для отладки.
#  *Иногда* repr может содержать достаточно информации для восстановления объекта.
# __str__ возвращает человеко-читаемое сообщение. Если __str__ не определён, то str использует repr.
class Person:  # A simple class with init, repr and str methods
    def __init__(self, name: str):
        self.name: str = name

    def __repr__(self):
        return f"Person '{self.name}'"

    def __str__(self):
        return f"{self.name}"

    def say_hi(self):
        print("Hi, my name is", self.name)


p = Person("Charlie")
p.say_hi()
print(repr(p))
print(str(p))


# @property
# https://docs.python.org/3/library/functions.html?highlight=property#property
# Декоратор @property используется для определения методов, доступных как поля. Таким образом операции чтения/записи поля можно обрамить
# дополнительной логикой, например, проверкой допустимых значений входного аргумента.

class Circle:
    def __init__(self, radius, max_radius):
        self._radius = radius
        self.max_radius = max_radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= self.max_radius:
            self._radius = value
        else:
            raise ValueError

    @property
    def area(self):
        return 2 * self.radius * math.pi


circle = Circle(10, 100)
circle.radius = 20  # OK
# circle.radius = 101  # Raises ValueError
print(circle.area)


# Обычный метод (т. е. не помеченный декораторами @staticmethod или @classmethod) имеет доступ к свойствам конкретного экземпляра класса.

# @staticmethod — метод, принадлежащий классу, а не экземпляру класса. Можно вызывать без создания экземпляра, т. к. метод
# не имеет доступа к свойствам экземпляра. При помощи @staticmethod помечают функционал, логически связанный с классом,
# но не требующий доступа к свойствам экземпляра.

# Если метод не должен иметь доступа к свойствам конкретного экземпляра класса (как @staticmethod), но должен иметь доступ к другим
# методам и переменным класса, то следует использовать @classmethod.

class B(object):
    def foo(self, x):
        print(f"Run foo({self}, {x})")

    @classmethod
    def class_foo(cls, x):
        print(f"Run class_foo({cls}, {x})")

    @staticmethod
    def static_foo(x):
        print(f"Run static_foo({x})")


b = B()
b.foo(1)
b.class_foo(1)
b.static_foo(1)

# У @classmethod первым параметром должен быть cls (класс), а у обычного метода - self (экземпляр класса).
# Для @staticmethod не требуется ни cls, ни self.
