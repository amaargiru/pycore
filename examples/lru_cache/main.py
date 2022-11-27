def mysum(n):
    if n == 1:
        return n
    print(f"'{n}'", end=" ")
    return n + mysum(n - 1)

mysum(5)
print("\n")
mysum(9)
print("\n")


import functools

@functools.lru_cache
def mysum2(n):
    if n == 1:
        return n
    print(f"'{n}'", end=" ")
    return n + mysum2(n - 1)

mysum2(5)
print("\n")
mysum2(9)
