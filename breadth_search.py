tree = [
    [1, 2],
    [3, 4], [5, 6],
    [7, 8], [9, 10], [11, 12], [13, 14],
    [], [], [], [], [], [], [], []
]

queue = [0]
while len(queue) > 0:
    print('before_queue')
    print(queue)

    index = queue.pop(0)

    print('index')
    print(index)
    print('after_queue')
    print(queue)

    # print(index, end=' ')

    for i in tree[index]:
        queue.append(i)
