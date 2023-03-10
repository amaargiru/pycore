# Утиная типизация итерируемых объектов

# Iterable (https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)
# Объект для предоставления возможности поочерёдного прохода по всем своим элементам должен реализовывать метод iter(), возвращающий
# итератор.

class MyIterable:
    def __init__(self, *args):
        self.a = list(args)

    def __iter__(self):
        return iter(self.a)


mi = MyIterable(1, 2, 3, 4)
print([el for el in mi])
print(1 in mi)


# Collection (https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection)
# Объект, предоставляющий возможность поочерёдного прохода по всем своим элементам и обладающий конечным размером.
# В дополнение к iter() должен быть реализован метод len(), возвращающий размер коллекции.

class MyCollection:
    def __init__(self, *args):
        self.a = list(args)

    def __iter__(self):
        return iter(self.a)

    def __len__(self):
        return len(self.a)


mc = MyCollection(1, 2, 3, 4)
print([el for el in mc])
print(1 in mc)
print(len(mc))
