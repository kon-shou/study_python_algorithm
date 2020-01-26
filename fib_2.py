memo = {1: 1, 2: 1}


def fib(n):
    if n in memo:
        return memo[n]

    memo[n] = fib(n - 2) + fib(n - 1)
    return memo[n]


# print(fib(10))
# print(memo.values())


def fib_loop(n):
    fib_arr = [1, 1]
    for i in range(2, n):
        fib_arr.append(fib_arr[i - 2] + fib_arr[i - 1])

    return fib_arr[n - 1]


print(fib_loop(100))
