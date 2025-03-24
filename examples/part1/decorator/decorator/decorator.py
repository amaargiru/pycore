import time


# Декораторы — это, по сути, своеобразные «обёртки», которые дают нам возможность делать что-либо до и после того,
# что сделает декорируемая функция, не изменяя её.
# Можно сказать, что декоратор является просто синтаксическим сахаром для конструкции вида:
# my_function = my_decorator(my_function)

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


# Разумеется, при последовательном применении нескольких декораторов играет роль порядок декорирования.
@makebold
@makeitalic
def hello():
    return "Hello, world!"


print(hello())


# Декоратор, подсчитывающий время работы оборачиваемой функции
def perf_counter(function):
    def counted(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(f"{time.perf_counter_ns() - start_time} ns")
        return res

    return counted


@perf_counter
def slow_sum(x, y):
    time.sleep(1)
    return x + y


print(slow_sum(1, 2))


# В декоратор можно передать и позиционные, и именованные аргументы — args и kwargs соответственно.
# Синтаксис декораторов с аргументами немного отличается — декоратор с аргументами должен возвращать функцию,
# которая принимает функцию и возвращает другую функцию.
def text_wrapper(wrap_text):
    def wrapped(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return f"{wrap_text}\n{result}\n{wrap_text}"

        return wrapper

    return wrapped


@text_wrapper('============')
def my_decorated_function(text):
    return text


print(my_decorated_function('Hello, world!'))
