from copy import copy, deepcopy


class A:
    def __init__(self, val: list):
        self.val = val

    def change_val(self, val: list):
        self.val = val


a = A(list("one"))

# Просто копирование ссылки на объект
b = a  # Assignment

# Создание нового объекта и копирование ссылок на объекты, найденные в изначальном объекте
c = copy(a)  # Shallow copy

# Создание нового объекта с последующим рекурсивным копированием содержащихся внутри объектов
d = deepcopy(a)  # Deep Copy

b.change_val(list("two"))
c.change_val(list("three"))
d.change_val(list("four"))

print(a.val, b.val, c.val, d.val)
print(id(a), id(b), id(c), id(d))
print(id(a.val[1]), id(c.val[1]))
