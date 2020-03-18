import functools

X, Y = 6, 5


@functools.lru_cache(maxsize=None)
def search(x, y):
    if (x == 0) and (y == 0):
        return 0

    if (x == 0) or (y == 0):
        return 1

    return search(x - 1, y) + search(x, y - 1)


print(search(X, Y))

print(search.cache_info())
