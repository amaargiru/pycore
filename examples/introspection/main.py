# Introspection

# Variables

# При вызове функции dir() без аргументов она возвращает список атрибутов (включая функции), доступных в локальной области видимости.
local_variables: list = dir()

# locals() возвращает словарь текущей локальной таблицы символов (атрибут __dict__). locals() эквивалентна vars() без аргумента.
local_vars: dict = locals()

# globals() возвращает словарь глобальной таблицы символов
global_variables: dict = globals()  # Dict of global variables.

print(local_variables)
print(local_vars)
print(global_variables)

# Attributes

# <list> = dir(<object>)                     # Names of object's attributes (incl. methods).
# <dict> = vars(<object>)                    # Dict of writable attributes. Also <obj>.__dict__.
# <bool> = hasattr(<object>, '<attr_name>')  # Checks if getattr() raises an AttributeError.
# value  = getattr(<object>, '<attr_name>')  # Raises AttributeError if attribute is missing.
# setattr(<object>, '<attr_name>', value)    # Only works on objects with '__dict__' attribute.
# delattr(<object>, '<attr_name>')           # Same. Also `del <object>.<attr_name>`.

# Parameters

# <Sig>  = inspect.signature(<function>)     # Function's Signature object.
# <dict> = <Sig>.parameters                  # Dict of Parameter objects.
# <memb> = <Param>.kind                      # Member of ParameterKind enum.
# <obj>  = <Param>.default                   # Default value or <Param>.empty.
# <type> = <Param>.annotation                # Type or <Param>.empty.
