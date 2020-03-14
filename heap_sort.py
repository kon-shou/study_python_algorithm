data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]


def parent_index(index):
    return (index - 1) // 2


# 親が子より大きくなる木構造を作る
for i in range(len(data)):
    j = i
    while j > 0:
        # 親が子より大きければ、問題なし
        if data[j] < data[parent_index(j)]:
            break
        # 親と交換
        data[parent_index(j)], data[j] = data[j], data[parent_index(j)]
        # 親の位置に移動
        j = parent_index(j)


def child_left_index(index):
    return 2 * index + 1


def child_right_index(index):
    return 2 * index + 2


# 木構造の末尾から走査を行う
for i in range(len(data) - 1, 0, -1):
    # ヒープの先頭と交換
    data[i], data[0] = data[0], data[i]
    j = 0
    while (child_left_index(j) < i) and (data[j] < data[child_left_index(j)]) \
            or (child_right_index(j) < i) and (data[j] < data[child_right_index(j)]):

        # 左下の方が大きい場合
        if (child_right_index(j) == i) or (data[child_left_index(j)] > data[child_right_index(j)]):
            # 左下と交換
            data[j], data[child_left_index(j)] = data[child_left_index(j)], data[j]
            # 左上に移動
            j = child_left_index(j)
        # 右下のほうが大きい場合
        else:
            # 右上と交換
            data[j], data[child_right_index(j)] = data[child_right_index(j)], data[j]
            # 右下に移動
            j = child_right_index(j)

print(data)
