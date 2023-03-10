import functools


def recursion_sum(n):
    if n == 1:
        return n
    print(n, end=" ")
    return n + recursion_sum(n - 1)


recursion_sum(5)
print("\n")
recursion_sum(9)
print("\n")


@functools.lru_cache
def recursion_sum2(n):
    if n == 1:
        return n
    print(n, end=" ")
    return n + recursion_sum2(n - 1)


recursion_sum2(5)
print("\n")
recursion_sum2(9)
