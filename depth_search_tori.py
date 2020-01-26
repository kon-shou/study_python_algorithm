tree = [
    [1, 2],
    [3, 4], [5, 6],
    [7, 8], [9, 10], [11, 12], [13, 14],
    [15], [], [], [], [], [], [], [],
    []
]


def search(pos):
    if len(tree[pos]) == 2:
        print('子が２')
        search(tree[pos][0])
        print(pos)
        search(tree[pos][1])
    elif len(tree[pos]) == 1:
        print('子が１')
        search(tree[pos][0])
        print(pos)
    else:
        print('子が０')
        print(pos)


search(0)
