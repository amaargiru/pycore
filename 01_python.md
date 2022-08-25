## **Ядро планеты Python**

## Структуры данных

### Массив <a name="basicarray"></a>  

Массив может быть одномерным, многомерным или массивом массивов.  
Количество измерений и длина каждого из измерений задаются, когда создается экземпляр массива. Эти значения нельзя изменить во время существования экземпляра.  
Все массивы реализуют _IList_ и _IEnumerable_. Одномерные массивы также реализуют _IList<T>_ и _IEnumerable<T>_.  

Для типов значений элементы массива инициализируются со значением по умолчанию.
Все ссылочные типы имеют значение null.  
Для типов nullable параметр HasValue имеет значение false, а для элементов будет установлено значение null.  

### Динамический массив <a name="basicdarray"></a>  

В C# это List\<T>. Реализует ICollection\<T>, IEnumerable\<T>, IList\<T>, IReadOnlyCollection\<T>, IReadOnlyList\<T>, ICollection, IEnumerable, IList.  

List\<T> реализован на базе массива, размер которого динамически увеличивается по мере необходимости.  

Имеет методы BinarySearch и Sort.  

### Односвязный список <a name="basicslist"></a>  

Односвязный список представляет набор связанных узлов, каждый из которых хранит собственно данные и ссылку на следующий узел. В практике малоприменим, но его любят использовать интервьюеры на собеседованиях, чтобы кандидат мог блеснуть своими алгоритмическими знаниями.  

### Двусвязный список <a name="basicdlist"></a>  

В C# - [LinkedList\<T>](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.linkedlist-1), гораздо практичнее и удобнее односвязного списка. Реализует ICollection\<T>, IEnumerable\<T>, IReadOnlyCollection\<T>, ICollection, IEnumerable, IDeserializationCallback, ISerializable.  


### Хэш-таблица <a name="basichashtable"></a>  

В C# это HashSet\<T>, Dictionary\<K,V> и OrderedDictionary\<T>. HashSet\<T>  Dictionary\<K,V> имеют [сходное быстродействие](https://stackoverflow.com/questions/2728500/hashsett-versus-dictionaryk-v-w-r-t-searching-time-to-find-if-an-item-exist) и оба сильно выигрывают у List\<T> на операциях поиска нужного значения.  

### Решение проблем вычисления хеша <a name="basichashtableproblem"></a>  

В HashSet\<T> объекты, имеющие одинаковый хеш, будут размещены в одной bucket (корзине). В идеале, для максимального ускорения поиска, желательно иметь один объект в каждой корзине, поэтому функцию вычисления хеша делают [позиционно-зависимой](https://stackoverflow.com/questions/7666509/hash-function-for-string), чтобы, например, хеш от строки "ab" отличался от хеша строки "ba".  

### Бинарное дерево <a name="basicbinarytree"></a>  

Иерархическая структура данных, в которой каждый узел имеет не более двух потомков. В C# это [SortedDictionary\<T>](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.sorteddictionary-2).  

### B-дерево (Би-дерево)<a name="basicbtree"></a>  

Сбалансированное дерево, оптимизированное для доступа к относительно медленным элементам памяти (например, дисковым структурам или индексам баз данных), как ветви, так и листья представляют собой списки (для того, чтобы можно было считать такой список в один проход для дальнейшего разбора в ОЗУ), но обычно различаются по структуре.  

### Красно-черное дерево <a name="basicrbtree"></a>  

Самобалансирующееся двоичное дерево поиска, позволяющее быстро выполнять основные операции дерева поиска: добавление, удаление и поиск узла. В коллекциях C# представлено SortedSet\<T>. Сбалансированность достигается за счёт введения дополнительного признака узла дерева — «цвета». Этот атрибут может принимать одно из двух возможных значений — «чёрный» или «красный». Листовые узлы КЧ деревьев не содержат данных, поэтому не требуют выделения памяти — достаточно просто записать в узле-предке нулевой указатель на потомка.

### АВЛ-дерево <a name="basicavltree"></a>  

В АВЛ-деревьях операции вставки и удаления работают медленнее, чем в красно-черных деревьях (при том же количестве листьев красно-чёрное дерево может быть выше АВЛ-дерева, но не более чем в 1,388 раза). Поиск же в АВЛ-дереве выполняется быстрее (максимальная разница в скорости поиска составляет 39 %).  

### Префиксное дерево <a name="basictrie"></a>  

Структура данных, позволяющая хранить ассоциативный массив, ключами которого являются строки.  

### Таблица выбора структуры данных <a name="basicstructselectiontable"></a>  

В квадратных скобках показан худший случай.

<style>
table th:first-of-type {
    width: 25%;
}
table th:nth-of-type(2) {
    width: 25%;
}
table th:nth-of-type(3) {
    width: 25%;
}
table th:nth-of-type(4) {
    width: 5%;
}
table th:nth-of-type(5) {
    width: 5%;
}
table th:nth-of-type(6) {
    width: 5%;
}
table th:nth-of-type(7) {
    width: 5%;
}
table th:nth-of-type(8) {
    width: 5%;
}
</style>

| Структура | Реализация | Применение | Индекс. | Поиск | Вставка | Удал. | Память |
| :- | :- | :- | :-: | :-: | :-: | :-: | :-: |
| Массив | Array,<br> SortedList (на базе двух массивов для ключей и значений),<br> Stack,<br> Queue,<br> PriorityQueue |  | 1 | n |  |  | n |
| Динамический массив | List\<T> |  | 1 | n | n | n | n |
| Односвязный список | ListDictionary | Не рекомендуется для применения, как и другие коллекции из пространства имен [System.Collections.Specialized](https://docs.microsoft.com/en-us/dotnet/api/system.collections.specialized) | n | n | 1 | 1 | n |
| Двусвязный список | [LinkedList\<T>](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.linkedlist-1) |  | n | n | 1 | 1 | n |
| Хэш таблица | HashSet\<T>, Dictionary\<K,V>, [OrderedDictionary\<T>](https://docs.microsoft.com/en-us/dotnet/api/system.collections.specialized.ordereddictionary) |  |  | 1<br> [n] | 1<br> [n] | 1<br> [n] | n |
| Бинарное дерево | [SortedDictionary\<T>](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.sorteddictionary-2) |  | logn<br> [n] | logn<br> [n] | logn<br> [n] | logn<br> [n] | n |
| [B-дерево](https://en.wikipedia.org/wiki/B-tree)<br> (Би-дерево) |  | Для памяти с медленным доступом | logn | logn | logn | logn | n |
| КЧ дерево | SortedSet\<T> |  | logn | logn | logn | logn | n |
| АВЛ дерево |  |  | logn | logn | logn | logn | n |
| Префиксное дерево |  | T9,<br> алгоритм [Ахо–Корасик](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm),<br> алгоритм [LZW](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch) |  | key | key | key |  |

## Где будет быстрее поиск, а где перебор и почему: dict, list, set, tuple?!!!

### List (список)


```python
a = []  # Создаем пустой список

a: list[int] = [10, 20]
b: list[int] = [30, 40]
a.append(50)  # Добавляем значение в конец списка
b.insert(2, 60)  # Вставляем значение по определенному индексу
print(a, b)

a += b
print(f"Add: {a}")

a.reverse()
b = list(reversed(a))  # reversed() возвращает итератор, а не список
print(f"Reverse: {a}, {b}")

b = sorted(a)  # Возвращает новый отсортированный список
a.sort()  # Модифицирует исходный список и не возвращает ничего
print(f"Sort: {a}, {b}")

s: str = "A whole string"
list_of_chars: list = list(s)
print(list_of_chars)
list_of_words: list = s.split()
print(list_of_words)

i: int = list_of_chars.index("w")  # Возвращает индекс первого вхождения искомого элемента или вызывает исключение ValueError
print(i)
list_of_chars.remove("w")  # Удаляет первое вхождение искомого элемента или вызывает исключение ValueError
e = list_of_chars.pop(9)  # Удаляет и возвращает значение, расположенное по индексу. pop() (без аргумента) удалит и вернет последний элемент списка
print(list_of_chars, e)
a.clear()  # Очистка списка
```

    [10, 20, 50] [30, 40, 60]
    Add: [10, 20, 50, 30, 40, 60]
    Reverse: [60, 40, 30, 50, 20, 10], [10, 20, 50, 30, 40, 60]
    Sort: [10, 20, 30, 40, 50, 60], [10, 20, 30, 40, 50, 60]
    ['A', ' ', 'w', 'h', 'o', 'l', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g']
    ['A', 'whole', 'string']
    2
    ['A', ' ', 'h', 'o', 'l', 'e', ' ', 's', 't', 'i', 'n', 'g'] r
    

### Dictionary (словарь)


```python
d = {}  # Создаем пустой словарь

d: dict[str, str] = {"Italy": "Pizza", "US": "Hot-Dog", "China": "Dim Sum"}  # Непосредственное создание словаря

k = ["Italy", "US", "China"]
v = ["Pizza", "Hot-Dog", "Dim Sum"]
d = dict(zip(k, v))  # Создание словаря из двух коллекций при помощи zip

k = d.keys()  # Коллекция ключей. Отражает изменения в основном словаре
v = d.values()  # Коллекция значений. Тоже отражает изменения в основном словаре
k_v = d.items()  # Кортежи ключ-значение, которые тоже отражают изменения в основном словаре

print(d)
print(k)
print(v)
print(k_v)

print(f"Mapping: {k.mapping['Italy']}")

d.update({"China": "Dumplings"})  # Добавление значение. При совпадении ключа старое значение будет перезаписано
print(f"Replace item: {d}")

c = d["China"]  # Читаем значение
print(f"Read item: {c}")

try:
    v = d.pop("Spain")  # Удаляет значение или вызывает исключение KeyError
except KeyError:
    print("Dictionary key doesn't exist")

# Примеры dict comprehension
b = {k: v for k, v in d.items() if "a" in k}  # Вернет новый словарь, отфильтрованный по значению ключа
print(b)

c = {k: v for k, v in d.items() if len(v) >= 7}  # Вернет новый словарь, отфильтрованный по длине значений
print(c)

d.clear() # Очистка списка
```

    {'Italy': 'Pizza', 'US': 'Hot-Dog', 'China': 'Dim Sum'}
    dict_keys(['Italy', 'US', 'China'])
    dict_values(['Pizza', 'Hot-Dog', 'Dim Sum'])
    dict_items([('Italy', 'Pizza'), ('US', 'Hot-Dog'), ('China', 'Dim Sum')])
    Mapping: Pizza
    Replace item: {'Italy': 'Pizza', 'US': 'Hot-Dog', 'China': 'Dumplings'}
    Read item: Dumplings
    Dictionary key doesn't exist
    {'Italy': 'Pizza', 'China': 'Dumplings'}
    {'US': 'Hot-Dog', 'China': 'Dumplings'}
    

## Как работает хэш-таблица (словарь)? Что такое коллизии и как с ними бороться?!!!

Что может являться ключом словаря? Что не может? Почему?

Ключом словаря может быть любой неизменяемый объект: число, строка, datetime, функция и даже модуль. Такие объекты имеют метод __hash__(), который однозначно сопоставляет объект с некоторым числом. По этому числу словарь ищет значение для ключа.

Списки, словари и множества изменяемы и не имеют метода хеширования. При подстановке их в словарь возникнет ошибка.

Хеш кортежа вычисляется рекурсивно по всем элементам. Так, кортеж

(1, (True, (42, ('hello', ))))
состоит только из неизменяемых элементов, поэтому может быть ключом. Однако, такой кортеж

(1, (True, (42, ({'hello': 'world'}, ))))
содержит глубоко внутри словарь, поэтому хеш не может быть рассчитан.

### defaultdict

The *defaultdict* will create any items that you try to access (provided of course they do not exist yet) without throws a KeyError.


```python
from collections import defaultdict

dd = defaultdict(int)  # defaultdict
print(dd[10])  # Печать int, будет выведен ноль, значение по умолчанию

dd = {}  # "Обычный" словарь
# print(dd[10])  # вызовет исключение KeyError
```

    0
    

### Counter (счетчик)

A Counter is a dict subclass for counting hashable objects, it is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.


```python
from collections import Counter

shirts_colors = ["red", "white", "blue", "white", "white", "black", "black"]
c = Counter(shirts_colors)
print(c)

c["blue"] += 1
print(f"After shopping: {c}")

# We can explain how Counter() works with defaultdict():
from collections import defaultdict

d = defaultdict(int)
for shirt in shirts_colors:
    d[shirt] += 1
d["blue"] += 1

print(d)
```

    Counter({'white': 3, 'black': 2, 'red': 1, 'blue': 1})
    After shopping: Counter({'white': 3, 'blue': 2, 'black': 2, 'red': 1})
    defaultdict(<class 'int'>, {'red': 1, 'white': 3, 'blue': 2, 'black': 2})
    

### Set (множество)


```python
big_cities: set["str"] = {"New-York", "Los Angeles", "Ottawa"}
american_cities: set["str"] = {"Chicago", "New-York", "Los Angeles"}

big_cities |= {"Sydney"}  # Add item (or you can use add())
american_cities |= {"Salt Lake City", "Seattle"}  # Add set (or you can use update())

print(big_cities, american_cities)

union_cities: set["str"] = big_cities | american_cities  # Or union()
intersected_cities: set["str"] = big_cities & american_cities  # Or intersection()
dif_cities: set["str"] = big_cities - american_cities  # Or difference()
symdif_cities: set["str"] = big_cities ^ american_cities  # Or symmetric_difference()

issub: bool = big_cities <= union_cities  # Or issubset()
issuper: bool = american_cities >= dif_cities  # Or issuperset()

print(union_cities)
print(intersected_cities)
print(dif_cities)
print(symdif_cities)

print(issub, issuper)

big_cities.add("London")  # Add items

big_cities.remove("Ottawa")  # Removes an item from the set if it is present or raises KeyError
big_cities.discard("Los Angeles")  # Remove an item from the set if it is present without raising KeyError
big_cities.pop()  # Remove and return a random item from the set or raises KeyError
big_cities.clear()  # Removes all items from the set
```

    {'Sydney', 'Ottawa', 'New-York', 'Los Angeles'} {'Chicago', 'Seattle', 'Salt Lake City', 'New-York', 'Los Angeles'}
    {'Ottawa', 'Chicago', 'Seattle', 'Salt Lake City', 'Los Angeles', 'Sydney', 'New-York'}
    {'New-York', 'Los Angeles'}
    {'Sydney', 'Ottawa'}
    {'Sydney', 'Ottawa', 'Chicago', 'Seattle', 'Salt Lake City'}
    True False
    

### Frozen Set

Frozen set is just an immutable and hashable version of a set object. Frozen set can be used as key in Dictionary or as element of another set.


```python
s = frozenset({"New-York", "Los Angeles", "Ottawa"})
```

### Tuple (кортеж)  
Tuple is an immutable and hashable list


```python
a = (2, 3)
b = ("Boson", "Higgs", 1.56e-22)

print(a, b)
```

    (2, 3) ('Boson', 'Higgs', 1.56e-22)
    

### Named Tuple (именованный кортеж)
Subclass of tuple with named elements


```python
from collections import namedtuple

rectangle = namedtuple('rectangle', 'length width')
r = rectangle(length = 1, width = 2)

print(r)
print(r.length)
print(r.width)
print(r._fields)
```

    rectangle(length=1, width=2)
    1
    2
    ('length', 'width')
    

### Enum


```python
from enum import Enum, auto
import random

class Currency(Enum):
    euro = 1
    us_dollar = 2
    yuan = auto()

# If there are no numeric values before auto(), it returns 1, otherwise it returns an increment of the last numeric value

local_currency = Currency.us_dollar  # Returns a member
print(local_currency)

local_currency = Currency["us_dollar"]  # Returns a member or raises KeyError
print(local_currency)

local_currency = Currency(2)  # Returns a member or raises ValueError
print(local_currency)

print(local_currency.name)
print(local_currency.value)

list_of_members = list(Currency)
member_names    = [e.name for e in Currency]
member_values   = [e.value for e in Currency]
random_member   = random.choice(list(Currency))

print(list_of_members, "\n",
      member_names, "\n",
      member_values, "\n",
      random_member)
```

    Currency.us_dollar
    Currency.us_dollar
    Currency.us_dollar
    us_dollar
    2
    [<Currency.euro: 1>, <Currency.us_dollar: 2>, <Currency.yuan: 3>] 
     ['euro', 'us_dollar', 'yuan'] 
     [1, 2, 3] 
     Currency.euro
    

### Range


```python

r1: range = range(11)  # Creates a sequence of numbers from 0 to 10
r2: range = range(5, 21) # Creates a sequence of numbers from 5 to 20
r3: range = range(20, 9, -2)  # Creates a sequence of numbers from 20 to 10 with step 2

print("To exclusive: ", end="")
for i in r1:
  print(f"{i} ", end="")

print("\nFrom inclusive to exclusive: ", end="")
for i in r2:
  print(f"{i} ", end="")

print("\nFrom inclusive to exclusive with step: ", end="")
for i in r3:
  print(f"{i} ", end="")

print(f"\nFrom = {r3.start}")
print(f"To = {r3.stop}")
```

    To exclusive: 0 1 2 3 4 5 6 7 8 9 10 
    From inclusive to exclusive: 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
    From inclusive to exclusive with step: 20 18 16 14 12 10 
    From = 20
    To = 9
    

### Dataclass  
Decorator that automatically generates init(), repr() and eq() special methods


```python
from dataclasses import dataclass
from decimal import *
from datetime import datetime

@dataclass
class Transaction:
    value: Decimal
    issuer: str = "Default Bank"
    dt: datetime = datetime.now()

t1 = Transaction(value=1000_000, issuer="Deutsche Bank", dt = datetime(2022, 1, 1, 12))
t2 = Transaction(1000)

print(t1)
print(t2)
```

    Transaction(value=1000000, issuer='Deutsche Bank', dt=datetime.datetime(2022, 1, 1, 12, 0))
    Transaction(value=1000, issuer='Default Bank', dt=datetime.datetime(2022, 8, 20, 16, 2, 23, 327826))
    

Objects can be made immutable with *frozen=True*.


```python
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    account: int

```

### Deque

A thread-safe list with efficient appends and pops from either side.


```python
from collections import deque
d = deque([1, 2, 3, 4], maxlen=1000)

d.append(5)  # Add element to the right side of the deque
d.appendleft(0)  # Add element to the left side of the deque by appending elements from iterable

d.extend([6, 7])  # Extend the right side of the deque
d.extendleft([-1, -2])  # Extend the left side of the deque
print(d)

a = d.pop()  # Remove and return an element from the right side of the deque. Can raise an IndexError
b = d.popleft()  # Remove and return an element from the left side of the deque. Can raise an IndexError
print(a, b)
print(d)
```

    deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7], maxlen=1000)
    7 -2
    deque([-1, 0, 1, 2, 3, 4, 5, 6], maxlen=1000)
    

### Queue

The queue module implements multi-producer, multi-consumer FIFO queues. It is especially useful in threaded programming when information must be exchanged safely between multiple threads. For LIFO queue use LifoQueue. For a priority queue use PriorityQueue.


```python
from queue import Queue
q = Queue(maxsize=1000)

q.put("eat", block=True, timeout=10)  # Put an element to the queue with 10 seconds timeuot, block if necessary until a free slot is available
q.put("sleep")  # Default values block=True, timeout=None
q.put("code")
q.put_nowait("repeat")  # Equivalent to put("repeat", block=False). Put an element on the queue if a free slot is immediately available, else raise the queue.Full exception
print(q.queue)

a = q.get(block=True, timeout=10)  # Remove and return an item from the queue
b = q.get()  # Default values block=True, timeout=None
c = q.get_nowait()  # Equivalent to get(False)
print(a, b, c, q.queue)
```

    deque(['eat', 'sleep', 'code', 'repeat'])
    eat sleep code deque(['repeat'])
    

### Array (массив)  
Object type that can only hold numbers of a predefined type.


```python
from array import array

a1 = array("l", [1, 2, 3, -4])  # Array from collection of numbers
a2 = array("b", b"1234567890")  # Array from bytes object
b = bytes(a2)

print(a1)
print(a2[0])
print(b)

print(a1.index(-4))  # Returns an index of a member or raises ValueError
```

    array('l', [1, 2, 3, -4])
    49
    b'1234567890'
    3
    

### Generator (генератор)

Any function that contains a yield statement returns a generator.


```python
def count(start, step):
    current = start
    while True:
        yield current
        current += step

c = count(100, 10)

print(next(c))
print(next(c))
print(next(c))
```

    100
    110
    120
    

## String (строка)


```python
se: str = ""  # Empty string
si: str = str(12345)  # Creates the string from int
sj: str = " ".join(["Follow", "the", "white", "rabbit"])  # Joins items using string as a separator
print(f"Joined string: {sj}")

is_contains: bool = "rabbit" in sj  # Checks if string contains a substring
is_startswith = sj.startswith("Foll")
is_endswith = sj.endswith("bbit")
print(f"is_contains = {is_contains}, is_startswith = {is_startswith}, is_endswith = {is_endswith}")

sr: str  = sj.replace("rabbit", "sheep")  # Replaces substrings. Also you can use times:  sr: str  = sj.replace("rabbit", "sheep", times)
print(f"After replace: {sr}")

i1 = sr.find("rabbit")  # Returns start index of the first match or -1. Also rfind()
i2 = sr.index("sheep")  #  Returns start index of the first match or raises ValueError. Also rindex()   
print(f"Start index of 'rabbit' is {i1}, start index of 'sheep' is {i2}")

d = str.maketrans({"a" : "x", "b" : "y", "c" : "z"})
st  = "abc".translate(d)
print(f"Translate string: {st}")

sr = sj[::-1]  # Reverse (Explanation: stackoverflow.com/questions/931092/reverse-a-string-in-python)
print(f"Reverse string: {sr}")
```

    Joined string: Follow the white rabbit
    is_contains = True, is_startswith = True, is_endswith = True
    After replace: Follow the white sheep
    Start index of 'rabbit' is -1, start index of 'sheep' is 17
    Translate string: xyz
    Reverse string: tibbar etihw eht wolloF
    

### lower(), upper(), capitalize() и title()


```python
s: str = "camelCase string"

print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
```

    camelcase string
    CAMELCASE STRING
    Camelcase string
    Camelcase String
    

### Property Methods

```text
+---------------+----------+----------+----------+----------+----------+
|               | [ !#$%…] | [a-zA-Z] |  [½¼¾]   |  [²³¹]   |  [0-9]   |
+---------------+----------+----------+----------+----------+----------+
| isprintable() |   yes    |   yes    |   yes    |   yes    |   yes    |
| isalnum()     |          |   yes    |   yes    |   yes    |   yes    |
| isnumeric()   |          |          |   yes    |   yes    |   yes    |
| isdigit()     |          |          |          |   yes    |   yes    |
| isdecimal()   |          |          |          |          |   yes    |
+---------------+----------+----------+----------+----------+----------+
```

*isspace()* checks for *[ \t\n\r\f\v\x1c-\x1f\x85…]*

### strip()


```python
s: str = "  ~~##A big blahblahblah##~~  "

s = s.strip()  # Strips all whitespace characters from both ends
print(s)

s = s.strip("~#")  # Strips all passed characters from both ends
print(s)

s = s.lstrip(" A")  # Strips all passed characters from left end
print(s)

s = s.rstrip("habl")  # Strips all passed characters from right end
print(s)

```

    ~~##A big blahblahblah##~~
    A big blahblahblah
    big blahblahblah
    big 
    

### split()


```python
s1: str = "Follow the white rabbit, Neo"

c1 = s1.split()  # Splits on one or more whitespace characters
print(c1)

c2 = s1.split(sep=", ", maxsplit=1)  # Splits on "sep" str at most "maxsplit" times
print(c2)

s2: str = "Beware the Jabberwock, my son!\n The jaws that bite, the claws that catch!"

c3 = s2.splitlines(keepends=False)  # On [\n\r\f\v\x1c-\x1e\x85\u2028\u2029] and \r\n.
print(c3)

# split() vs rsplit()

c4 = s2.split(maxsplit=2)
c5 = s2.rsplit(maxsplit=2)

print(c4, c5)
```

    ['Follow', 'the', 'white', 'rabbit,', 'Neo']
    ['Follow the white rabbit', 'Neo']
    ['Beware the Jabberwock, my son!', ' The jaws that bite, the claws that catch!']
    ['Beware', 'the', 'Jabberwock, my son!\n The jaws that bite, the claws that catch!'] ['Beware the Jabberwock, my son!\n The jaws that bite, the claws', 'that', 'catch!']
    

### ord(), chr()


```python
s1: str = "abcABC!"

for ch in s1:
    print(f"{ch} -> {ord(ch)}")  # Returns an integer representing the Unicode character

nums = [72, 101, 108, 108, 111, 33]

for num in nums:
    print(f"{num} -> {chr(num)}")
```

    a -> 97
    b -> 98
    c -> 99
    A -> 65
    B -> 66
    C -> 67
    ! -> 33
    72 -> H
    101 -> e
    108 -> l
    108 -> l
    111 -> o
    33 -> !
    

## Regex

Argument flags=re.IGNORECASE can be used with all functions


```python
import re

s1: str = "123 abc ABC 456"

m1 = re.search("[aA]", s1)  # Searches for first occurrence of the pattern; search() return None if it can't find a match
print(m1)
print(m1.group(0))

m2 = re.match("[aA]", s1)  # Searches at the beginning of the text; match() return None if it can't find a match
print(m2)

c1: list = re.findall("[aA]", s1)  # Returns all occurrences as strings
print(c1)

def replacer(s):  # replacer() can be a function that accepts a match object and returns a string
    return chr(ord(s[0]) + 1)  # Next symbol in alphabet

s2 = re.sub("\w", replacer, s1)  # Substitutes all occurrences with 'replacer'
print(s2)

c2 = re.split("\d", s1)
print(c2)

iter = re.finditer("\D", s1)  # Returns all occurrences as match objects

for ch in iter:
    print(ch.group(0), end= "")
```

    <re.Match object; span=(4, 5), match='a'>
    a
    None
    ['a', 'A']
    234 bcd BCD 567
    ['', '', '', ' abc ABC ', '', '', '']
     abc ABC 

### Match Object


```python
import re

m3 = re.match(r"(\w+) (\w+)", "John Connor, leader of the Resistance")

s3: str = m3.group(0)  # Returns the whole match
s4: str = m3.group(1)  # Returns part in the first bracket
t1: tuple = m3.groups()  # Returns all bracketed parts
start: int = m3.start()  # Returns start index of the match
end: int = m3.end()  # Returns exclusive end index of the match
t2: tuple[int, int] = m3.span()  # Return the 2-tuple (start, end)

print (f"{s3}\n {s4}\n {t1}\n {start}\n {end}\n {t2}\n")
```

    John Connor
     John
     ('John', 'Connor')
     0
     11
     (0, 11)
    
    

### JSON

Human-readable text format to store and transmit data objects.


```python
import json

d: dict = {1: "Lemon", 2: "Apple", 3: "Banana!"}

object_as_string: str = json.dumps(d, indent=2)
print(object_as_string)

restored_object = json.loads(object_as_string)

# Write object to JSON file
with open("1.json", 'w', encoding='utf-8') as file:
    json.dump(d, file, indent=2)

# Read object from JSON file
with open("1.json", encoding='utf-8') as file:
    restored_from_file = json.load(file)
    
print(restored_from_file)

```

    {
      "1": "Lemon",
      "2": "Apple",
      "3": "Banana!"
    }
    {'1': 'Lemon', '2': 'Apple', '3': 'Banana!'}
    

### Pickle

Бинарный формат для хранения и транспортировки структур данных.


```python
import pickle

d: dict = {1: "Lemon", 2: "Apple", 3: "Banana!"}

# Запись объекта в бинарный файл
with open("1.bin", "wb") as file:
    pickle.dump(d, file)

# Чтение объекта из файла
with open("1.bin", "rb") as file:
    restored_from_file = pickle.load(file)

print(restored_from_file)
```

    {1: 'Lemon', 2: 'Apple', 3: 'Banana!'}
    

### Protocol Buffers
Если вы хотите передавать и хранить данные, используя универсальную структуру, одинаково хорошо понимаемую всеми языками программирования (как JSON) и занимающую мало места (как Pickle), то можно посмотреть в сторону Protocol Buffers ([Wikipedia](https://en.wikipedia.org/wiki/Protocol_Buffers), [примеры для Python](https://developers.google.com/protocol-buffers/docs/pythontutorial)). Есть еще альтернативы, например, [FlatBuffers](https://google.github.io/flatbuffers/), [Apache Avro](https://avro.apache.org/) или [Thrift](https://thrift.apache.org/).

### Bytes

Bytes object is an immutable sequence of single bytes. Mutable version is called bytearray.


```python

### Encode
b1 = bytes([1, 2, 3, 4])  # Ints must be in range from 0 to 255
b2 = "The String".encode('utf-8')
b3 = (-1024).to_bytes(4, byteorder='big', signed=True)  # byteorder="big"/"little"/"sys.byteorder", signed=False/True
b4 = bytes.fromhex('FEADCA')  # Hex pairs can be separated by spaces
b5 = bytes(range(10,30,2))

print(b1, b2, b3, b4, b5)

### Decode
c: list = list(b"\xfc\x00\x00\x00\x00\x01")  # Returns ints in range from 0 to 255
s: str = b'The String'.decode("utf-8")
b: int = int.from_bytes(b"\xfc\x00", byteorder='big', signed=False)  # byteorder="big"/"little"/"sys.byteorder", signed=False/True
s2: str = b"\xfc\x00\x00\x00\x00\x01".hex(" ")  # Returns a string of hexadecimal pairs, hex pairs can be separated by spaces

print(c, s, b, s2)

with open("1.bin", "wb") as file:  # Write bytes to file
    file.write(b1)

with open("1.bin", "rb") as file:  # Read bytes from file
    b6 = file.read()

print(b6)
```

    b'\x01\x02\x03\x04' b'The String' b'\xff\xff\xfc\x00' b'\xfe\xad\xca' b'\n\x0c\x0e\x10\x12\x14\x16\x18\x1a\x1c'
    [252, 0, 0, 0, 0, 1] The String 64512 fc 00 00 00 00 01
    b'\x01\x02\x03\x04'
    

### Struct

Module that performs conversions between a sequence of numbers and a bytes object. System’s type sizes and byte order are used by default.


```python
from struct import pack, unpack, iter_unpack

b = pack(">hhll", 1, 2, 3, 4)
print(b)

t = unpack(">hhll", b)
print(t)

i = pack("ii", 1, 2) * 5
print(i)

print(list(iter_unpack('ii', i)))
```

    b'\x00\x01\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04'
    (1, 2, 3, 4)
    b'\x01\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00'
    [(1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]
    

## Datetime

Module *datetime* provides *date*, *time*, *datetime* and *timedelta*. All are immutable and hashable

### Constructors


```python
from datetime import date, time, datetime, timedelta

d: date = date(year=1964, month=9, day=2)
t: time  = time(hour=12, minute=30, second=0, microsecond=0, tzinfo=None, fold=0)
dt: datetime = datetime(year=1964, month=9, day=2, hour=10, minute=30, second=0)
td: timedelta = timedelta(weeks=1, days=1, hours=12, minutes=13, seconds=14)

print (f"{d}\n {t}\n {dt}\n {td}")
```

    1964-09-02
     12:30:00
     1964-09-02 10:30:00
     8 days, 12:13:14
    

### Now


```python
from datetime import date, time, datetime
import pytz

d: date  = date.today()
dt1: datetime = datetime.today()
dt2: datetime = datetime.utcnow()
dt3: datetime = datetime.now(pytz.timezone('US/Pacific'))

print (f"{d}\n {dt1}\n {dt2}\n {dt3}")

```

    2022-08-20
     2022-08-20 16:02:24.484302
     2022-08-20 11:02:24.484301
     2022-08-20 04:02:24.484301-07:00
    

### Timezone


```python
from datetime import date, time, datetime, timedelta, tzinfo
from dateutil.tz import UTC, tzlocal, gettz, datetime_exists, resolve_imaginary

tz1: tzinfo = UTC  # UTC timezone

tz2: tzinfo = tzlocal()  # Local timezone
tz3: tzinfo = gettz()  # Local timezone

tz4: tzinfo = gettz("America/Chicago")  # "Asia/Kolkata" etc. See full list at en.wikipedia.org/wiki/List_of_tz_database_time_zones

local_dt = datetime.today()
utc_dt = local_dt.astimezone(UTC)  # Convert local datetime to UTC datetime

print (f"{tz1}\n {tz2}\n {tz3}\n {tz4}\n {local_dt}\n {utc_dt}")
```

    tzutc()
     tzlocal()
     tzlocal()
     tzfile('US/Central')
     2022-08-20 16:02:24.547197
     2022-08-20 11:02:24.547197+00:00
    

### Encode

Python uses the Unix Epoch: "1970-01-01 00:00 UTC"


```python
from datetime import datetime
from dateutil.tz import tzlocal

dt1: datetime = datetime.fromisoformat("2021-10-04 00:05:23.555+00:00")  # Raises ValueError
dt2: datetime = datetime.strptime("21/10/04 17:30", "%d/%m/%y %H:%M")   # Datetime from str, according to format (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
dt3: datetime = datetime.fromordinal(100000)  # 100000th day after 1.1.0001
dt4: datetime = datetime.fromtimestamp(20_000_000.01)  # Local datetime from seconds since the Epoch

tz2: tzinfo = tzlocal()
dt5: datetime = datetime.fromtimestamp(300_000_000, tz2)  # Aware datetime from seconds since the Epoch

print (f"{dt1}\n {dt2}\n {dt3}\n {dt4}\n {dt5}")
```

    2021-10-04 00:05:23.555000+00:00
     2004-10-21 17:30:00
     0274-10-16 00:00:00
     1970-08-20 16:33:20.010000
     1979-07-05 10:20:00+05:00
    

### Decode


```python
from datetime import datetime

dt1: datetime = datetime.today()

s1: str = dt1.isoformat()
s2: str = dt1.strftime("%d/%m/%y %H:%M")  # Outputting datetime object to string (format: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
i: int = dt1.toordinal()  # Days since Gregorian NYE 1, ignoring time and tz
a: float = dt1.timestamp()  # Seconds since the Epoch

print (f"{dt1}\n {s1}\n {s2}\n {i}\n {a}")
```

    2022-08-20 16:02:24.687670
     2022-08-20T16:02:24.687670
     20/08/22 16:02
     738387
     1660993344.68767
    

### Arithmetics


```python
from datetime import date, time, datetime, timedelta
from dateutil.tz import UTC, tzlocal, gettz, datetime_exists, resolve_imaginary

d: date  = date.today()
dt1: datetime = datetime.today()
dt2: datetime = datetime(year=1981, month=12, day=2)
td1: timedelta = timedelta(days=5)
td2: timedelta = timedelta(days=1)

d = d + td1  # date = date ± timedelta
dt3 = dt1 - td1  # datetime = datetime ± timedelta

td3 = dt1 - dt2  # timedelta = datetime - datetime

td4 = 10 * td1  # timedelta = const * timedelta
c: float = td1/td2  # timedelta/timedelta

print (f"{d}\n {dt3}\n {td3}\n {td4}\n {c}")
```

    2022-08-25
     2022-08-15 16:02:24.750712
     14871 days, 16:02:24.750712
     50 days, 0:00:00
     5.0
    

## File

### Open

Open the file and return a corresponding file object.


```python
f = open("f.txt", mode='r', encoding="utf-8", newline=None)

print(f.read())
```

    Hello from file!
    


*encoding=None* means that the default encoding is used, which is platform dependent. Best practice is to use *encoding="utf-8"* whenever possible.  
*newline=None* means all different end of line combinations are converted to '\n' on read, while on write all '\n' characters are converted to system's default line separator.  
*newline=""* means no conversions take place, but input is still broken into chunks by readline() and readlines() on every "\n", "\r" and "\r\n".  

### Modes

"r" - Read (default)  
"w" - Write (truncate)  
"x" - Write or fail if the file already exists  
"a" - Append  
"w+" - Read and write (truncate)  
"r+" - Read and write from the start  
"a+" - Read and write from the end  
"t" - Text mode (default)  
"b" - Binary mode (`'br'`, `'bw'`, `'bx'`, …)  

### Exceptions

*FileNotFoundError* can be raised when reading with "r" or "r+".  
*FileExistsError* can be raised when writing with "x".  
*IsADirectoryError* and *PermissionError* can be raised by any.  
*OSError* is the parent class of all listed exceptions.  

### Read from file


```python
with open("f.txt", encoding="utf-8") as f:
    chars = f.read(5)  # Reads chars/bytes or until EOF
    print(chars)

    f.seek(0)  # Moves to the start of the file. Also seek(offset) and seek(±offset, anchor), where anchor is 0 for start, 1 for current position and 2 for end

    lines: list[str] = f.readlines()  # Also readline()
    print(lines)
```

    Hello
    ['Hello from file!']
    

### Write to file


```python
with open("f.txt", "w", encoding="utf-8") as f:
    f.write("Hello from file!")  # Also f.writelines(<collection>)
    # f.flush() for flushes write buffer; runs every 4096/8192 B
```

## Paths


```python
from os import getcwd, path, listdir
from pathlib import Path

s1: str = getcwd()  # Returns the current working directory
print(s1)

s2: str = path.abspath("f.txt")  # Returns absolute path
print(s2)

s3: str = path.basename(s2)  # Returns final component of the path
s4: str = path.dirname(s2)  # Returns path without the final component
t1: tuple = path.splitext(s2)  # Splits on last period of the final component
print(s3, s4, t1)

p = Path(s2)
st = p.stat()
print(st)

b1: bool = p.exists()
b2: bool = p.is_file()
b3: bool = p.is_dir()
print(b1, b2, b3)

c: list = listdir(path=s1)  # Returns filenames located at path
print(c)

s5: str = p.stem  # Returns final component without extension
s6: str  = p.suffix  # Returns final component's extension
t2: tuple = p.parts  # Returns all components as strings
print(s5, s6, t2)
```

    c:\Works\amaargiru\ipycs
    c:\Works\amaargiru\ipycs\f.txt
    f.txt c:\Works\amaargiru\ipycs ('c:\\Works\\amaargiru\\ipycs\\f', '.txt')
    os.stat_result(st_mode=33206, st_ino=25051272927278718, st_dev=3628794147, st_nlink=1, st_uid=0, st_gid=0, st_size=16, st_atime=1658139122, st_mtime=1658139122, st_ctime=1654437943)
    True True False
    ['.git', '.gitignore', '1.bin', '1.json', 'convert_nb_to_md.bat', 'f.txt', 'LICENSE', 'pycallgraph3.png', 'PYCS.ipynb', 'README.md']
    f .txt ('c:\\', 'Works', 'amaargiru', 'ipycs', 'f.txt')
    

## Data querying

### Sum, Count, Min, Max


```python
a: list[int] = [1, 2, 3, 4, 5, 2, 2]

s = sum(a)
print(s)

c = a.count(2)  # Returns number of occurrences
print(c)

mn = min(a)
print(mn)

mx = max(a)
print(mx)
```

    19
    3
    1
    5
    

### List comprehension
An elegant approach to create a new list based on the values of an existing list.


```python
# new_list = [expression for member in iterable (if conditional)]

fruits: list = ["Lemon", "Apple", "Banana", "Kiwi", "Watermelon", "Pear"]

e_fruits = [fruit for fruit in fruits if "e" in fruit]
#                                     ☝ if conditional
print(e_fruits)

upper_fruits = [fruit.upper() for fruit in fruits]
#                     ☝ expression
print(upper_fruits)

# Split a list into equal sized chunks
chunk_len = 2
chunk_fruits = [fruits[i:i + chunk_len] for i in range(0, len(fruits), chunk_len)]
print(chunk_fruits)

```

    ['Lemon', 'Apple', 'Watermelon', 'Pear']
    ['LEMON', 'APPLE', 'BANANA', 'KIWI', 'WATERMELON', 'PEAR']
    [['Lemon', 'Apple'], ['Banana', 'Kiwi'], ['Watermelon', 'Pear']]
    

### Dictionary comprehension
Creating new dictionaries from existing dictionaries and iterables. A dictionary comprehension is very much like a list comprehension, but we get a dictionary at the end of it, so we need to be assigning key value pairs instead of only values.


```python
# new_dict = {expression for member in iterable (if conditional)}

d: dict[str, str] = {"Italy": "Pizza", "US": "Hot-Dog", "China": "Dim Sum", "South Korea": "Kimchi"}  # Create a dictionary

d2: dict[str, str] = {k: v for k, v in d.items() if "i" in v}  ## Select only elements that contain a letter "i" in value
print(d2)

```

    {'Italy': 'Pizza', 'China': 'Dim Sum', 'South Korea': 'Kimchi'}
    

### bisect и бинарный поиск


```python
import bisect

a: list[int] = [12, 6, 8, 19, 1, 33]

a.sort()
print(f"Sorted: {a}")

print(bisect.bisect(a, 19))  # Locate the insertion point for value in a list to maintain sorted order

bisect.insort(a, 15)  # Insert value in a list in sorted order
print(a)

# Binary search

from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)

    pos = bisect_left(a, x, lo, hi)
    return pos if pos != hi and a[pos] == x else -1

print(binary_search(a, 15))
```

    Sorted: [1, 6, 8, 12, 19, 33]
    5
    [1, 6, 8, 12, 15, 19, 33]
    4
    

### Pairwise


```python
import itertools

a = [1, 2, 3, 4, 5]
p = itertools.pairwise(a)  # Returns successive overlapping pairs

print(list(p))
```

    [(1, 2), (2, 3), (3, 4), (4, 5)]
    

### Шифрование и дешифрование


```python
# pip install pycryptodomex
import hashlib

from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad

def encrypt_data(password: str, raw_data: bytes) -> bytes:
    res = bytes()
    try:
        key = hashlib.sha256(password.encode()).digest()
        align_raw = pad(raw_data, AES.block_size)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphered_data = cipher.encrypt(align_raw)
        res = iv + ciphered_data
    except Exception as e:
        print(f"Encrypt error: {str(e)}")
    return res

def decrypt_data(password: str, encrypted_data: bytes) -> bytes:
    res = bytes()
    try:
        key = hashlib.sha256(password.encode()).digest()
        iv = encrypted_data[:AES.block_size]
        ciphered_data = encrypted_data[AES.block_size:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypt_data = cipher.decrypt(ciphered_data)
        res = unpad(decrypt_data, AES.block_size)
    except Exception as e:
        print(f"Decrypt error: {str(e)}")
    return res

def encrypt_file(src_file: str, dst_file: str, password: str) -> bool:
    try:
        with open(src_file, "rb") as reader, open(dst_file, "wb") as writer:
            data = reader.read()
            data_enc = encrypt_data(password, data)
            writer.write(data_enc)
            writer.flush()
            print(f"{src_file} encrypted into {dst_file}")
        return True
    except Exception as e:
        print(f"Encrypt_file error: {str(e)}")
        return False

def decrypt_file(src_file: str, dst_file: str, password: str) -> bool:
    try:
        with open(src_file, "rb") as reader, open(dst_file, "wb") as writer:
            data = reader.read()
            data_decrypt = decrypt_data(password, data)
            writer.write(data_decrypt)
            writer.flush()
            print(f"{src_file} decrypted into {dst_file}")
        return True
    except Exception as e:
        print(f"Decrypt file error: {str(e)}")
        return False

if __name__ == '__main__':
    mes: bytes = bytes("A am the Message", "utf-8")
    passw: str = "h3AC3TsU8TECvyCqd5Q5WUag5uXLjct2"
    print(f"Original message: {mes}")

    # Encrypt message
    enc: bytes = encrypt_data(passw, mes)
    print(f"Encrypted message: {enc}")

    # Decrypt message
    dec: bytes = decrypt_data(passw, enc)
    print(f"Decrypted message: {dec}")

```

    Original message: b'A am the Message'
    Encrypted message: b'\xdf\xb9j:\xb8;%\xe9\xae\xfe\xd2 \x81w%"\x88[\x9e*\xd4\x8e\x1b\xa5K)\x19\xce]\xd7\x1e]\xb0\x10\x84\x18\x1fOn\xdd\xe3\xf9}\x92F\xc1DB'
    Decrypted message: b'A am the Message'
    

## Exceptions

### Catching exceptions

Basic Example


```python
a: float = 0
b: float = 0

try:
    b: float = 1/a
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

    Error: division by zero
    

More complex example. Code inside the *else* block will only be executed if *try* block had no exceptions. Code inside the *finally* block will always be executed (unless a signal is received).


```python
import traceback

a: float = 0
b: float = 0

try:
    b: float = 1/a
except ZeroDivisionError as e:
    print(f"Error: {e}")
except ArithmeticError as e:
    print(f"We have a bit more complicated problem: {e}")
except Exception as serious_problem:  # Catch all exceptions
    print(f"I don't really know what is going on: {traceback.print_exception(serious_problem)}")
else:
    print("No errors!")
finally:
    print("This part is always called")
```

    Error: division by zero
    This part is always called
    

### Вызов исключений


```python
from decimal import *

def div(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ValueError("Second argument must be non-zero")
    return a/b


try:
    c: Decimal = div(1, 0)
except ValueError:
    print("We have ValueError, as a planned!")
    # raise # We can re-raise exception
```

    We have ValueError, as a planned!
    

### Встроенные исключения
```text
BaseException
 +-- SystemExit                   # Raised by the sys.exit() function
 +-- KeyboardInterrupt            # Raised when the user press the interrupt key (ctrl-c)
 +-- Exception                    # User-defined exceptions should be derived from this class
      +-- ArithmeticError         # Base class for arithmetic errors
      |    +-- ZeroDivisionError  # Dividing by zero
      +-- AttributeError          # Attribute is missing
      +-- EOFError                # Raised by input() when it hits end-of-file condition
      +-- LookupError             # Raised when a look-up on a collection fails
      |    +-- IndexError         # A sequence index is out of range
      |    +-- KeyError           # A dictionary key or set element is missing
      +-- NameError               # An object is missing
      +-- OSError                 # Errors such as “file not found”
      |    +-- FileNotFoundError  # File or directory is requested but doesn't exist
      +-- RuntimeError            # Error that don't fall into other categories
      |    +-- RecursionError     # Maximum recursion depth is exceeded
      +-- StopIteration           # Raised by next() when run on an empty iterator
      +-- TypeError               # An argument is of wrong type
      +-- ValueError              # When an argument is of right type but inappropriate value
           +-- UnicodeError       # Encoding/decoding strings to/from bytes fails
```

### Выход из программы при помощи вызова исключения SystemExit


```python
import sys

# sys.exit()  # Exits with exit code 0 (success)
# sys.exit(777)  # Exits with passed exit code
```

### Исключения, определяемые пользователем


```python
class MyException(Exception):
    pass

raise MyException("My car is broken")
```


    ---------------------------------------------------------------------------

    MyException                               Traceback (most recent call last)

    c:\Works\amaargiru\ipycs\PYCS.ipynb Ячейка 100 in <cell line: 4>()
          <a href='vscode-notebook-cell:/c%3A/Works/amaargiru/ipycs/PYCS.ipynb#Y166sZmlsZQ%3D%3D?line=0'>1</a> class MyException(Exception):
          <a href='vscode-notebook-cell:/c%3A/Works/amaargiru/ipycs/PYCS.ipynb#Y166sZmlsZQ%3D%3D?line=1'>2</a>     pass
    ----> <a href='vscode-notebook-cell:/c%3A/Works/amaargiru/ipycs/PYCS.ipynb#Y166sZmlsZQ%3D%3D?line=3'>4</a> raise MyException("My car is broken")
    

    MyException: My car is broken


### Exception Object

```python
arguments = <name>.args
exc_type = <name>.__class__
filename = <name>.__traceback__.tb_frame.f_code.co_filename
func_name = <name>.__traceback__.tb_frame.f_code.co_name
line = linecache.getline(filename, <name>.__traceback__.tb_lineno)
error_msg = ''.join(traceback.format_exception(exc_type, <name>, <name>.__traceback__))
```

## Математика

### Базовая математика


```python
from math import pi

a: float = pi ** 2  # Or pow(pi, 2)
print(f"Power: {a}")

b: float = round(pi, 2)
print(f"Round: {b}")

c: int = round(256, -2)
print(f"Int round: {c}")

d: float = abs(-pi)
print(f"Abs: {d}")

e: float = abs(10+10j)  # Or e: float = abs(complex(real=10, imag=10))
print(f"Complex abs: {e}")

```

    Power: 9.869604401089358
    Round: 3.14
    Int round: 300
    Abs: 3.141592653589793
    Complex abs: 14.142135623730951
    

### Побитовые операции


```python
a: int = 0b01010101
b: int = 0b10101010

print(f"And: 0b{a&b:08b}")
print(f"Or: 0b{a|b:08b}")
print(f"Xor: 0b{a^b:08b}")
print(f"Left shift: 0b{a << 4:08b}")
print(f"Right shift: 0b{b >> 4:08b}")
print(f"Not: 0b{~a:08b}")
```

    And: 0b00000000
    Or: 0b11111111
    Xor: 0b11111111
    Left shift: 0b10101010000
    Right shift: 0b00001010
    Not: 0b-1010110
    

### Подсчет битов


```python
a: int = 4242
print(f"{a} in binary format: 0b{a:b}")

c = a.bit_count()  # Returns the number of ones in the binary representation of the absolute value of the integer
print(f"Bit count: {c}")
```

    4242 in binary format: 0b1000010010010
    Bit count: 4
    

### Fractions


```python
from fractions import Fraction

f = Fraction("0.2").as_integer_ratio()

print(f)
```

    (1, 5)
    

### Euclidean distance between two points


```python
import math

p1 = (0.22, 1, 12)
p2 = (-0.12, 3, 7)

print(math.dist(p1, p2))
```

    5.39588732276722
    

## Random


```python
import random

rf: float = random.random()  # A float inside [0, 1)
print(f"Single float random: {rf}")

ri: int = random.randint(1, 10)  # An int inside [from, to]
print(f"Single int random: {ri}")

rb = random.randbytes(10)
print(f"Random bytes: {rb}")

rc: str = random.choice(["Alice", "Bob", "Maggie", "Madhuri Dixit"])
print(f"Random choice: {rc}")

rs: str = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print(f"Random list without duplicates: {rs}")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List before shuffle: {a}")
random.shuffle(a)
print(f"List after shuffle: {a}")

```

    Single float random: 0.9024807633898538
    Single int random: 7
    Random bytes: b'>\xe0^\x16PX\xf8E\xf8\x98'
    Random choice: Bob
    Random list without duplicates: [5, 10, 3, 6, 1]
    List before shuffle: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    List after shuffle: [10, 4, 6, 5, 1, 8, 3, 9, 7, 2]
    

## Profiling

### Stopwatch


```python
from time import time
start_time = time()

j: int = 0
for i in range(10_000_000):  # Long operation
    j = i ** 2

duration = time() - start_time
print(f"{duration} seconds")
```

    2.2923033237457275 seconds
    

### High performance


```python
from time import perf_counter
start_time = perf_counter()

j: int = 0
for i in range(10_000_000):  # Long operation
    j = i ** 2

duration = perf_counter() - start_time
print(f"{duration} seconds")
```

    2.3540456001646817 seconds
    

### timeit

Try to avoid a number of common traps for measuring execution times


```python
from timeit import timeit

def long_pow():
    j: int = 0
    for i in range(1000_000):  # Long operation
        j = i ** 2

timeit("long_pow()", number=10, globals=globals(), setup='pass')
```




    1.8552540000528097



### Call Graph

Generates a PNG image of the call graph with highlighted bottlenecks


```python
from pycallgraph3 import PyCallGraph
from pycallgraph3.output import GraphvizOutput

def long_pow():
    j: int = 0
    for i in range(1000_000):  # Long operation
        j = i ** 2

def short_pow():
    j: int = 0
    for i in range(1000):  # Short operation
        j = i ** 2

with PyCallGraph(output=GraphvizOutput()):
    # Code to be profiled
    long_pow()
    short_pow()
    # This will generate a file called pycallgraph3.png
```

<img src="pycallgraph3.png" style="height:400px">

## asyncio!!!

В JavaScript async / await сделаны жадными как Promise. При вызове async функции автоматически создается задача и отправляется в очередь на исполнение в event loop. await, в свою очередь, просто ждёт результат.

В питоне асинхронщину задизайнили иначе - лениво.

Вызов async функции возвращает объект - корутину, - которая ни чего не делает.

asyncio.run() создаёт event loop, запускает (корневую) корутину и блокирует поток до получения результата.

await запускает корутину изнутри другой корутины в текущем event loop и ждёт результат.

Для запуска корутины без ожидания (как это делает Promise) используется asyncio.create_task(coro). Либо asyncio.gather(*aws), если надо запустить сразу несколько. Нужно только следить, чтобы ссылка на возвращаемое значение сохранялась до конца вычисления, иначе его пожрет GC и все оборвется на самом интересном месте (промис бы отработал до конца не смотря ни на что).

В JS только один event loop, поэтому было вполне разумно закопать его внутрь promise / async / await как деталь реализации, упростив работу прикладному программисту. В питоне отзеркалили более ранний вариант корутин на генераторах, дали возможность использовать разные event loop и выставили все кишки наружу.

## Сборщик мусора!!!  
 Garbage collection, reference counting

## Как передаются значения аргументов в функцию или метод?!!!

### Итераторы

### Генераторы
https://xakep.ru/2014/10/06/generatora-iteratory-python/  

Итерация и генераторы
В чем отличие [x for x in y] от (x for x in y)?

Первое выражение возвращает список, второе – генератор.

Что особенного в генераторе?

Генератор хранит в памяти не все элементы, а только внутреннее состояние для вычисления очередного элемента. На каждом шаге можно вычислить только следующий элемент, но не предыдущий. Пройти генератор в цикле можно только один раз.

Как объявить генератор?

использовать синтаксис (x for x in seq)
оператор yield в теле функции вместо return
встроенная функция iter, которая вызывает у объекта метод __iter__(). Этот метод должен возвращать генератор.
Как получить из генератора список?

Передать его в конструктор списка: list(x for x in some_seq). Важно, что после этого по генератору уже нельзя будет итерироваться.

Можно ли извлечь элемент генератора по индексу?

Нет, будет ошибка. Генератор не поддерживает метод __getitem__.


Здесь важно, чтобы кандидат понимал различие и мог с той или иной степенью погружения рассказать про эти различия. Если кратко, то итератор в Python – это любой объект, который использует метод next() для получения следующего значения последовательности. Генератор – функция, которая производит или выдает последовательность значений с использованием метода yield. Концептуально, итератор — это механизм поэлементного обхода данных, а генератор позволяет отложено создавать результат при итерации. Генератор может создавать результат на основе какого-то алгоритма или брать элементы из источника данных (коллекция, файлы, сетевое подключения и др.) и изменять их.


### Декораторы

Что такое декораторы?

Декоратор в широком смысле – паттерн проектирования, когда один объект изменяет поведение другого. В Питоне декоратор, как правило, это функция A, которая принимает функцию B и возвращает функцию C. При этом функция C задействует в себе функцию B.

Задекорировать функцию значит заменить ее на результат работы декоратора.

Что может быть декоратором? К чему может быть применен декоратор?

Декоратором может быть любой вызываемый объект: функция, лямбда, класс, экземпляр класса. В последнем случае определите метод __call__.

Применять декоратор можно к любому объекту. Чаще всего к функциям, методам и классам. Декорирование встречается настолько часто, что под него выделен особый оператор @.

def auth_only(view):
    ...

@auth_only
def dashboard(request):
    ...
Если бы оператора декорирования не существовало, мы бы записали код выше так:

def auth_only(view):
    ...

def dashboard(request):
    ...

dashboard = auth_only(dashboard)
Что будет, если декоратор не возвращает ничего?

Если в теле функции нет оператора return, вызов вернет None. Помним, результат декоратора замещает декорируемый объект. В нашем случае декоратор вернет None и функция, которую мы декорируем, тоже станет None. При попытке вызвать ее после декорирования получим ошибку NoneType is not callable.

В чем отличие @foobar от @foobar()?

Первое – обычное декорирование функцией foobar.

Второй случай – декорирование функцией, которую вернет вызов foobar. По-другому это называется параметрический декоратор или фабрика декораторов. См. следующий вопрос.

Что такое фабрика декораторов?

Это функция, которая возвращает декоратор. Такой декоратор редко помещают в отдельную переменную. Вместо этого декорируют результатом вызова фабрики декораторов.

Например, вам нужен декоратор для проверки прав. Логика проверки одинакова, но прав может быть много. Чтобы не плодить копипасту, напишем фабрику декораторов.

from functools import wraps

def has_perm(perm):
    def decorator(view):
        @wraps(view)
        def wrapper(request):
            if perm in request.user.permissions:
                return view(request)
            else:
                return HTTPRedirect('/login')
        return wrapper
    return decorator

@has_perm('view_user')
def users(request):
    ...
Зачем нужен @wraps? functools.wraps

wraps – декоратор из стандартной поставки Питона, модуль functools. Он назначает функции-врапперу те же поля __name__, __module__, __doc__, что и у исходной функции, которую вы декорируете. Это нужно для того, чтобы после декорирования функция-враппер не выглядела в стектрейсах как исходная функция.

Можно ли использовать несколько декораторов для одной функции?  
Можно ли создать декоратор из класса?  

!!!Написать параметризированный декоратор, который печатает время выполнения декорированной функции. Параметр декоратора — точность округления в миллисекундах  
https://habr.com/ru/post/141411/  
https://habr.com/ru/post/141501/


## introspection

(использование dir(), dir, hasattr(), getattr())

Как получить список атрибутов объекта?

Функция dir возвращает список строк – полей объекта. Поле __dict__ содержит словарь вида {поле -> значение}.

### Одинарное (_) и двойное (__) подчеркивания

Python не использует спецификаторы доступа, такие как private, public, protected и т. д. Однако, в нем есть имитации поведения переменных путем использования одинарного (protected) или двойного подчеркивания (private) в качестве префикса к именам переменных. По умолчанию переменные без подчеркивания являются общедоступными.

Поле класса с одним лидирующим подчеркиванием говорит о том, что параметр используется только внутри класса. При этом он доступен для обращения извне.

class Foo(object):
    def __init__(self):
        self._bar = 42

Foo()._bar  
42  
Современные IDE вроде PyCharm подсвечивают обращение к полю с подчеркиванием, но ошибки в процессе исполнения не будет.

Поля с двойным подчеркиванием доступны внутри класса, но недоступны извне. Это достигается хитрым приемом: интерпретатор назначает таким полям имена вида _<ClassName>__<fieldName> (name mangling). Зная это правило, можно получить значение скрытого поля вне класса, но это смотрится очень уродливо.

class Foo(object):
    def __init__(self):
        self.__bar = 42

Foo().__bar  
  AttributeError: 'Foo' object has no attribute '__bar'  
Foo()._Foo__bar  
  42  


## Что такое MRO? Какая разница между MRO2 и MR3 (diamond problem)?!!!

Возможно ли множественное наследование? Что такое MRO?

Да, можно указать более одного родителя в классе потомка.

MRO – method resolution order, порядок разрешения методов. Алгоритм, по которому следует искать метод в случае, если у класса два и более родителей. Алгоритм линеизирует граф наследования. Коротко можно описать так: ищи слева направо. Поэтому чем правее стоит класс, тем меньше у него приоритет при поиске метода.

## Метаклассы!!!  

Что такое метакласс, переменная цикла?
Какие задачи решали с помощью метаклассов?

https://proglib.io/p/metaclasses-in-python  
https://habr.com/ru/post/145835/  

## PEP8!!!

Инструменты проверки code style!!!
https://proglib.io/p/python-code-analysis

Разница между is и ==?  
Разница между __init __ () и __new __ ()?  
В чем разница между потоками и процессами?  
Какие есть виды импорта?  
Что такое класс, итератор, генератор?  
В чем разница между итераторами и генераторами?  
В чем разница между staticmethod и classmethod?  
Как работают dict comprehension, list comprehension и set comprehension?  


### lambda-функции

Это анонимные функции. Они не резервируют имени в пространстве имен. Лямбды часто передают в функции map, reduce, filter.

Лямбды в Питоне могут состоять только из одного выражения. Используя синтаксис скобок, можно оформить тело лямбды в несколько строк.

Допустимы ли следующие выражения?

nope = lambda: pass
riser = lambda x: raise Exception(x)
Нет, при загрузке модуля выскочит исключение SyntaxError. В теле лямбды может быть только выражение. pass и raise являются операторами.


Что означает *args, **kwargs и как они используются?
Выражения *args и **kwargs объявляют в сигнатуре функции. Они означают, что внутри функции будут доступны переменные с именами args и kwargs (без звездочек). Можно использовать другие имена, но это считается дурным тоном.

args – это кортеж, который накапливает позиционные аргументы. kwargs – словарь позиционных аргументов, где ключ – имя параметра, значение – значение параметра.

Важно: если в функцию не передано никаких параметров, переменные будут соответственно равны пустому кортежу и пустому словарю, а не None.



Как создается объект в Python, для чего __new__, зачем __init__?  
Как работает thread locals?  
Как передаются аргументы функций в Python (by value or reference)?  
Что такое type annotation?  
Статические анализаторы: Flake8, Pylint, Radon  
Что такое @property?  
Каким образом можно запустить код на Python параллельно?  
Как работать с stdlib?  
Что такое дескрипторы?  

Какой будет результат операции -12 % 10?  
Какой будет результат операции -12 // 10?  
Какая последовательность вызова операторов в выражении a * b * c?  
Что делает функция id()?  
Для чего зарезервировано ключевое слово yield?  
В чем разница между __iter__ и __next__?
Что такое синхронный код? А асинхронный? Как написать асинхронное приложение?
Что такое проверка типов? Какие есть типы в Python?
Как осуществляется управление памятью в Python?

Как можно расширить зону видимости глобальных переменных на другие модули?
Как создать класс без инструкции class?

Как внедрить в программу расширения, написанные на языках C или C++? Что позволяет использовать библиотеки C-языков, что дает возможность управления ресурсами на более низком уровне? Конечно же, кандидат должен знать, что за такое отвечает интерпретатор CPython.



Почему def foo(bar=[]): плохо? Приведите пример плохого случая. Как исправить?
Почему нельзя сделать пустой список аргументом по умолчанию?  

Функция создается однажды при загрузке модуля. Именованные параметры и их дефолтные значения тоже создаются один раз и хранятся в одном из полей объекта-функции.

В нашем примере bar равен пустому списку. Список – изменяемая коллекция, поэтому значение bar может изменяться от вызова к вызову. Пример:

def foo(bar=[]):
    bar.append(1)
    return bar
foo()
[1]
foo()
[1, 1]
foo()
[1, 1, 1]
Хорошим тоном считается указывать параметру пустое неизменяемое значение, например 0, None, '', False. В теле функции проверять на заполненность и создавать новую коллекцию:

def foo(bar=None):
    if bar is None:
        bar = []
    bar.append(1)
    return bar
foo()
[1]
foo()
[1]
foo()
[1]


### GIL

Global Interpreter Lock. Особенность интерпретатора, когда одновременно может исполняться только один тред. Все это время остальные треды простаивают. GIL есть не только в Питоне, но и в других скриптовых языках, например, Руби.

Причина существования GIL в том, что для этих интерпретаторов еще не найден безопасный способ согласовывать изменения данных. Например, если один тред удалит все элемены из списка, а второй начнет итерацию по нему, гарантированно произойдет ошибка.

GIL работает так: на каждый тред выделяется некоторый квант времени. Он измеряется в машинных единицах “тиках” и по умолчанию равен 100. Как только на тред было потрачено 100 тиков, интерпретатор бросает этот тред и переключается на второй, тратит 100 тактов на него, затем третий, и так по кругу. Этот алгоритм гарантрует, что всем тредам будет выделено ресурсов поравну.

Проблема в том, что из-за GIL далеко не все задачи могут быть решены в тредах. Напротив, их использование чаще всего снижает быстродействие программы. С использованием тредов требуется следить за доступом к общим ресурсам: словарям, файлам, соединением к БД.


### Классы, объекты

Что такое магические методы, для чего нужны?

Магическими метода называют методы, имена которых начинаются и заканчиваются двойным подчеркиванием. Магические они потому, что почти никогда не вызываются явно. Их вызывают встроенные функции или синтаксические конструкции. Например, функция len() вызывает метод __len__() переданного объекта. Метод __add__(self, other) вызывается автоматически при сложении оператором +.

Перечислим некоторые магические методы:

__init__: конструктор класса
__add__: сложение с другим объектом
__eq__: проверка на равенство с другим объектом
__cmp__: сравнение (больше, меньше, равно)
__iter__: при подстановке объекта в цикл
Как в классе сослаться на родительский класс?

Функция super принимает класс и экземпляр:

class NextClass(FirstClass):
    def __init__(self, x):
        super(NextClass, self).__init__()
        self.x = x

### Контекстный менеджер

В питоне есть оператор with. Размещенный внутри код выполняется с особенностью: до и после гарантированно срабатывают события входа в блок withи выхода из него. Объект, который определяет логику событий, называется контекстным менеджером.

На уровне класса события определены методами __enter__ и __exit__. Первый срабатывает в тот момент, когда ход исполнения программы переходит внутрь with. Метод может вернуть значение. Оно будет доступно низлежащему внутри блока with коду.

__exit__ срабатывает в момент выхода блока, в т.ч. и по причине исключения. В этом случае в метод будет передана тройка значений (exc_class, exc_instance, traceback).

Самый распространённый контекстный менеджер – класс, порожденный функцией open. Он гарантирует, что файл будет закрыт даже в том случае, если внутри блока возникнет ошибка.

Старайтесь выходить из контекстного менеджера как можно быстрее, чтобы освобождать контекст и ресурсы.

with open('file.txt') as f:
    data = f.read()
process_data(data)
В примере выше мы вышли из блока with сразу же после прочтения файла. Обработка данных происходит в основном блоке программы.

Контекстные менеджеры можно использовать для временной замены параметров, переменных окружения, транзакций БД.

Что такое контекстный менеджер в Python? Чем он отличается от конструкции try ... finally?
Какие функции нужно переопределить в классе А, чтобы экземпляры этого класса могли реализовать протокол контекстного менеджера?

Напишем свой контекстный менеджер


Прокомментировать выражение object() == object()

Всегда ложь, поскольку по умолчанию объекты сравниваются по полю id (адрес в памяти), если только не переопределен метод __eq__.

Как удаляется объект?


### \_\_slots\_\_

Классы хранят поля и их значения в секретном словаре dict. Поскольку словарь – изменяемая структура, вы можете на лету добавлять и удалять из класса поля. Параметр slots в классе жестко фиксирует набор полей класса. Слоты используются когда у класса может быть очень много полей, например, в некоторых ORM, либо когда критична производительность, потому что доступ к слоту срабатывает быстрее, чем поиск в словаре.

Слоты активно используются в библиотеках requests и falcon.

Недостатки: нельзя присвоить классу поле, которого нет в слотах. Не работают методы __getattr__ и __setattr__.


### Многопоточность

Многопоточность достигается модулем Threading. Это нативные Posix-треды. Такие треды исполняются операционной системой, а не виртуальной машиной.

В чем отличие тредов от мультипроцессинга?

Главное отличие в разделении памяти. Процессы независимы друг от друга, имеют раздельные адресные пространства, идентификаторы, ресурсы. Треды исполняются в совместном адресном пространстве, имеют общий доступ к памяти, переменным, загруженным модулям.

Какие задачи хорошо параллелятся, какие плохо?

Те задачи, которые порождают долгий IO. Когда тред упирается в ожидание сокета или диска, интерпретатор бросает этот тред и стартует следующий. Это значит, не будет простоя из-за ожидания. Наоборот, если ходить в сеть в одном треде (в цикле), то каждый раз придется ждать ответа.

Однако, если затем в треде обрабатывает полученные данные, то выполнятся будет только он один. Это не только не даст прироста в скорости, но и замедлит программу из-за переключения на другие треды.

Короткий ответ: хорошо ложатся на треды задачи по работе с сетью. Например, выкачать сто урлов. Полученные данные обрабатывайте вне тредов.

Нужно посчитать 100 уравнений. Делать это в тредах или нет?

Нет, потому что в этой задаче нет ввода-вывода. Интерпретатор только будет тратить лишнее время на переключение тредов. Сложные математические задачи лучше выносить в отдельные процессы, либо использовать фреймворк для распределенных задач Celery, либо подключать как C-библиотеки.

Треды в Питоне — это нативные треды или нет?

Да, это нативные Posix-совместимые треды, которые исполняются на уровне операционной системы.

Понимание что такое heap dump и thread dump.

понимание многопоточности, способов ей управлять и проблем, с этим связанных (синхронизации, локи, race condition и т.д.);

### Рекурсия

Рекурсия – определение функции через саму себя. Логика рекурсивной функции как правило состоит из двух ветвей. Длинная ветвь вызывает эту же функцию с другими параметрами, чтобы накопить результат. Короткая ветвь определяет критерий выхода из рекурсии.

Рекурсия упрощает код и делает его декларативным. Рекурсия поощряет мыслить функционально и избегать побочных эффектов.

Неоптимизированная рекурсия приводит к накладным расходам ресурсов. При большом количестве итераций можно превысить лимит на число рекурсивных вызовов (recursion depth limit reached).

Что такое хвостовая рекурсия?

Это особый вид рекурсии, когда функция заканчивается вызовом самой себя без дополнительных операторов. Когда это условие выполняется, компилятор разворачивает рекурсию в цикл с одним стек-фреймом, просто меняя локальные переменные от итерации к итерации.

Так, классическое определение рекурсивного факториала return N * fact(N - 1) не поддерживает хвостовую рекурсию, потому что для каждого стек-фрейма придется хранить текущее значение N.

Чтобы сделать рекурсии хвостовой, добавляют параметры-аккумуляторы. Благодаря им функция знает о своем текущем состоянии. Пусть параметр acc по умолчанию равен 1. Тогда запись с хвостовой рекурсией будет выглядеть так:

def fact(N, acc=1):
    if N == 1:
        return acc
    else:
        return fact(N - 1, acc * N)


### Копирование объектов

В Python оператор присваивания (=) не копирует объекты. Вместо этого он создает связь между существующим объектом и именем целевой переменной. Чтобы создать копии объекта в Python, необходимо использовать модуль copy. Более того, существует два способа создания копий для данного объекта с помощью модуля copy.

Shallow Copy – это побитовая копия объекта. Созданный скопированный объект имеет точную копию значений в исходном объекте. Если одно из значений является ссылкой на другие объекты, копируются только адреса ссылок на них.
Deep Copy – рекурсивно копирует все значения от исходного объекта к целевому, т. е. дублирует даже объекты, на которые ссылается исходный объект.

## Источники  
Официальная документация Python [docs.python.org](https://docs.python.org/), включающая [The Python Standard Library](https://docs.python.org/3/library/index.html).  
Весьма подробное руководство (совсем уж базовый синтаксис не включен): [Comprehensive Python Cheatsheet](https://github.com/gto76/python-cheatsheet).  
Руководство с включением базового синтаксиса: [Python Cheatsheet](https://github.com/wilfredinni/python-cheatsheet). Включает практические Jupiter [Notebooks](https://github.com/wilfredinni/python-cheatsheet/tree/master/jupyter_notebooks).  
Сипсок библиотек и фреймворков: [Awesome Python](https://github.com/vinta/awesome-python).  
Около-питоновские практические советы (pip, virtualenv, pyInstaller и т. д.): ["The Hitchhiker’s Guide to Python"](https://github.com/realpython/python-guide).  
Мануал для начинающих дата-сайентистов: [Joel Grus, "Data Science from Scratch"](https://github.com/joelgrus/data-science-from-scratch).  
Руководство для начинающих: ["Python Notes for Professionals"](https://goalkicker.com/PythonBook/).  
Руководство для опытных программистов: ["Python 3 Patterns, Recipes and Idioms"](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/index.html).  
