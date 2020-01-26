import math


def get_prime(n):
    if n <= 1:
        return []
    prime = [2]
    limit = int(math.sqrt(n))
    print(limit)

    # 奇数のリスト作成
    data = [i for i in range(3, n + 1, 2)]
    while limit > data[0]:
        print('prime')
        print(prime)
        print('data')
        print(data)
        prime.append(data[0])
        # 割り切れない数だけを取り出す
        data = [j for j in data if j % data[0] != 0]

    return prime + data


print(get_prime(101))
