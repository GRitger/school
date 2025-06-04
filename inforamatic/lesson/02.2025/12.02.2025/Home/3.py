from functools import lru_cache


def g(x):
    return x + 3, x * 2


@lru_cache(None)
def f(x, y):
    if x >= 50 or y >= 50:
        return "+"
    if any(f(i, y) == "+" for i in g(x)) or any(f(x, i) == "+" for i in g(y)):
        return "p1"
    if all(f(i, y) == "p1" for i in g(x)) and all(f(x, i) == "p1" for i in g(y)):
        return "v1"
    if any(f(i, y) == "v1" for i in g(x)) or any(f(x, i) == "v1" for i in g(y)):
        return "p2"
    if all(f(i, y) in ["p1", "p2"]  for i in g(x)) and all(f(x, i) in ["p1", "p2"]  for i in g(y)):
        return "v2"


for i in range(1, 27):
    if f(i, 23) == "v2":
        print(i, f(i, 23))
