def convert(n, base):
    result = ''

    while n > 0:
        result = str(n % base) + result
        n //= base

    return result


m = 18
print(convert(m, 2))
print(convert(m, 3))
print(convert(m, 8))
