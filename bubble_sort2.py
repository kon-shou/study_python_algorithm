data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

change = True
for i in range(len(data)):
    # 確定済みでないリストで１回も交換が行われなかった場合、そのリストはソート済みである
    if not change:
        break
    change = False

    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            change = True

    print('最後尾の' + str(i) + '個が確定')
    print(data)

print(data)
