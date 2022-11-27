# декораторы — это, по сути, просто своеобразные «обёртки», которые дают нам возможность делать что-либо до и после того,
# что сделает декорируемая функция, не изменяя её.

# Да, всё действительно так просто! decorator — просто синтаксический сахар для конструкций вида:
# another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)

# Декораторы — это просто pythonic-реализация паттерна проектирования «Декоратор».

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


# Следует помнить о том, что порядок декорирования важен

@makebold
@makeitalic
def hello():
    return "hello habr"


print(hello())  # выведет <b><i>hello habr</i></b>


# Декоратор — это паттерн проектирования (design pattern) в Python, а также функция второго уровня, то есть принимающая другие функции
# в качестве переменных и возвращающая их.
# И в сам декоратор, и в функцию-обёртку можно передать и позиционные, и именованные аргументы — args и kwargs соответственно.
# Декораторы работают не только с функциями, но и с классами и методами.

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    return 'всем привет'


print(say_hi())

import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res

    return wrapped


@time_of_function
def funct(first, second):
    return bin(int(first, 2) + int(second, 2))


print(funct("111", "0000"))


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time() - t))
        return res

    return tmp


@timer
def func(x, y):
    return x + y


func(1, 2)


def my_decorator(input_arg):
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return f'{input_arg}\n{result}\n{input_arg}'

        return wrapper

    return the_real_decorator


@my_decorator('-------------')
def my_decorated_function(input):
    return input


print(my_decorated_function('Hello, World!'))
