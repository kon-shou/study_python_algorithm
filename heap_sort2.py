def heapify(data, i):
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2
    max_index = len(data) - 1
    min_value_index = i

    # 左の子ノードのほうが小さい場合
    if left_child_index <= max_index and data[min_value_index] > data[left_child_index]:
        min_value_index = left_child_index
    # 右の子ノードのほうが小さい場合
    if right_child_index <= max_index and data[min_value_index] > data[right_child_index]:
        min_value_index = right_child_index
    if min_value_index != i:
        data[i], data[min_value_index] = data[min_value_index], data[i]
        heapify(data, min_value_index)

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

print('reversed(range(len(data) // 2))')
print(list(reversed(range(len(data) // 2))))

for i in reversed(range(len(data) // 2)):
    heapify(data, i)

print(data)
