data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(1, len(data)):
    temp = data[i]
    j = i - 1
    while j >= 0:
        # 例えば、tempが4かつj=2の場合
        # 1, 3, 5, 5...となり、1,3は見る必要が無い
        if data[j] < temp:
            break
        data[j + 1] = data[j]
        j -= 1

    data[j + 1] = temp

print(data)
