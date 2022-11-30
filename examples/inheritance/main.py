# Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, staff_num, email):
        super().__init__(name, age)
        self.staff_num = staff_num
        self.email = email


# Multiple Inheritance

class PrivateStaffData:
    def __init__(self, private_email):
        self.private_email = private_email


class PublicStaffData:
    def __init__(self, work_email):
        self.work_email = work_email


class StaffData(PrivateStaffData, PublicStaffData):
    def __init__(self, private_email, work_email):
        super().__init__()


# Порядок разрешения методов (method resolution order) позволяет Питону выяснить, из какого класса-предка нужно вызывать метод,
# если он не обнаружен непосредственно в классе-потомке.

print(StaffData.mro())

# MRO строит иерархию наследования таким образом, чтобы более специфичные методы класса-потомка перекрывали менее специфичные методы
# класса-предка. MRO строит упорядоченный список классов (линеаризация класса), в которых будет производиться поиск метода слева направо.
# Для решения проблемы ромбовидной структуры (которая неявно присутствует даже в простейшем случае, так как все классы наследуются
# от object) линеаризация должна быть монотонной. Монотонность — свойство, которое требует соблюдения в линеаризации класса-потомка
# того же порядка следования классов-прародителей, что и в линеаризации класса-родителя.
# Линеаризация по сути является топологической сортировкой (https://en.wikipedia.org/wiki/Topological_sorting). В ранних версиях Python
# использовался алгоритм DLR, сейчас в ходу C3-линеаризация (https://en.wikipedia.org/wiki/C3_linearization).

# Если после удовлетворения свойства монотонности остаётся больше одного варианта линеаризации, то применяется порядок локального
# старшинства (local precedence ordering), т. е. порядок соблюдения для классов-родителей в линеаризации класса-потомка того же порядка,
# что и при его объявлении. Например, если класс объявлен как D(A, B, C), то в линеаризации D класс A должен стоять раньше B,
# а класс B — раньше C.

# Если разрешение всех конфликтов при линеаризации невозможно, то остается три пути:
# 1 - переменой мест классов-предков в объявлении класса-потомка (но это помогает далеко не всегда);
# 2 - пересмотр иерархии наследования;
# 3 - определение своей собственной линеаризации через метаклассы при помощи метода mro(cls), но надо быть готовым к тому, что будет
# использован менее специфичный метод класса-родителя вместо более специфичного метода класса-потомка. При задании своей собственной
# линеаризации Python отключает встроенные проверки.

# @abstractmethod
# Абстрактный класс в Python - аналог интерфейса в других языках, например, в C# - класс, содержащий только сигнатуры методов,
# без реализации. Реализация методов переложена на классы-потомки. Задача абстрактного класса соответствует задаче интерфейса -
# *обязать* классы-потомки реализовывать *все* методы, заложенные в классе-родителе.

import abc


class AbstractClass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def return_anything(self):
        return


class ConcreteClass(AbstractClass):

    def return_anything(self):
        return 42


c = ConcreteClass()
print(c.return_anything())

# Если не специфицировать return_anything() в ConcreteClass, при попытке вызвать c.return_anything() будет выброшено исключение
# TypeError: Can't instantiate abstract class ConcreteClass with abstract method return_anything
