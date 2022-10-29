Пайтон джуньор плюс, или Карта Сокровищ

### Введение

Добрый день! Меня зовут Михаил Емельянов, по профессии я программист программ, а эту небольшую памятку по базовым возможностям языка Python меня сподвиг написать довольно существенный, на мой взгляд, разрыв между декларируемыми объемами всевозможных курсов программирования и требованиями реальных, даже достаточно скромнооплачиваеых вакансий.

Пользуясь аналогиями из игрового мира, можно сказать, что начинающий программист зачастую стоит на берегу озера кипящей лавы, в центре которого находится остров со столь вожделенными вакансиями, а промежуточные островки, по которым надо перепрыгивать, постепенно наращивая свои навыки в последовательных мини-квестах, либо отсутствуют, либо расположены несистемно и хаотично, либо достаточно ровная их последовательность обрывается, так и не успев помочь отойти сколько-нибудь далеко от берега. Давайте попробуем построить дорожку островков-подсказок, ряд которых, хоть и не без усилий, позволит-таки нам достичь цели.

Небольшое отступление про формат Jupiter Notebooks, на случай, если раньше вам не приходилось иметь с ним дела. Jupiter позволяет перемешивать текстовые заметки, исходные коды и результаты вывода программ.  
Здесь вы видите текст, который выглядит как обычная статья, но это только потому, что исходный Jupiter Notebook был при помощи nbconvert преобразован в Markdown. На самом деле **все примеры кода интерактивны, вы можете их менять, дополнять и вообще крутить как угодно**, разбираясь в тонкостях Python; поэтому многие используемые методы не «разжеваны» (да такой задачи и не ставилось), Jupiter сам по себе лучший самоучитель. Исходные тексты лежат на [github/amaargiru/pycore](https://github.com/amaargiru/pycore).

Для работы с Jupiter вы можете воспользоваться [VS Code](https://code.visualstudio.com/), JetBrains [IntelliJ](https://www.jetbrains.com/ru-ru/idea/) или каким-нибудь онлайн-инструментом, самым известным из которых являятся [Google Colab](https://colab.research.google.com/).

В этой стать 100 % есть ошибки и неточности самых разных калибров, так что, если что-то углядите, не стесняйтесь выражаться в личку, в комментариях, на почту war4one@gmail.com, а если чувствуете в себе Силу — смело форкайте репу и пишите туда всё, что считаете нужным, все исправления и дополнения бурно приветствуются.

Погружаясь в Python, не забывайте про прекрасную официальную документацию [docs.python.org](https://docs.python.org/). Изучив её, хотя бы по диагонали, и постепенно углубляясь в нужные разделы, вы сможете убедиться, что многие «хаки», «открытия» и прочие неочевидные вещи уже давно разжеваны, описаны и имеют подробные примеры применения.

Также я бы рекомендовал для изучения базового синтаксиса Python на полную катушку использовать [leetcode.com](https://leetcode.com/problemset/all/?difficulty=EASY&page=1&status=NOT_STARTED). Если отфильтровать задачи по уровню «Easy», а потом добавить дополнительную сортировку по столбцу «Acceptance», то перед вами предстанет не волчий оскал соревновательной платформы, а ванильный букварь с плавно нарастающим уровнем задачек.

Что ж, пожалуй, довольно запрягать. Погнали!  

### Оглавление

```mermaid
flowchart TD
Data_Structures==>Data_Management==>Data_Flows==>OOP

subgraph Data_Structures
direction LR
List(list) -.-> Tuple -.-> Dict -.-> Set -.-> Array -.-> Linked_List -.->Tree -.-> Python_specific_data_structures
subgraph Tuple
direction LR
tuple(tuple)
namedtuple(namedtuple)
end
subgraph Dict
direction LR
dict(dict)
HashProblem("Проблема вычисления хеша")
defaultdict(defaultdict)
Counter
end
subgraph Set
direction LR
set(set)
FrozenSet("frozen set")
end
subgraph Array
direction LR
array(array)
bytes(bytes)
bytearray(bytearray)
end
subgraph Linked_List
direction LR
SinglyLinkedList("Singly linked list")
subgraph Doubly_Linked_List
direction LR
deque(deque)
Queue(Queue)
end
end
subgraph Tree
direction LR
tree(tree)
heap(heap)
B-tree(B-tree)
RedBlackTree("Red–black tree")
AVLTree("AVL tree")
trie(trie)
end
subgraph Python_specific_data_structures
direction LR
enum(enum)
range(range)
dataclass(dataclass)
struct(struct)
string(string)
datetime(datetime)
end
end

subgraph Data_Management
slice(slice)
subgraph Sorting
direction LR
sort(sort)
sorted(sorted)
end
bisect(bisect)
subgraph Comprehension
direction LR
listcomprehension(list)
dictcomprehension(dict)
setcomprehension(set)
end
functools
datetime_management
string_management
re
end

subgraph Data_Flows
itertools
enumerate
generator
subgraph Decorator
direction LR
decorator(decorator)
LRUCache("LRU Cache")
param_decorator("Параметризованный декоратор")
end
context("Контекстный менеджер (with)")
end

subgraph OOP
subgraph Class
direction LR
Comparable(Comparable)
Hashable(Hashable)
Sortable(Sortable)
Callable(Callable)
end
__slots__
object_copy("Копирование объектов")
MRO
metaprogramming("Метапрограммирование")

end

classDef dashed stroke-dasharray:5 5
class B-tree dashed;
class RedBlackTree dashed;
class AVLTree dashed;
class trie dashed;
class SinglyLinkedList dashed;
```
