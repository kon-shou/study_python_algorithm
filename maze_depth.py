maze = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 9, 0, 0, 0, 9, 9, 0, 9, 9, 9],
    [9, 0, 9, 9, 0, 9, 0, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 9, 0, 0, 9, 9, 0, 9, 9],
    [9, 9, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9],
    [9, 0, 0, 0, 9, 0, 9, 0, 0, 9, 1, 9],
    [9, 0, 9, 0, 0, 0, 0, 9, 0, 0, 9, 9],
    [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 0, 9],
    [9, 0, 9, 0, 9, 0, 9, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]


def search(vertical_i, horizontal_i, depth):
    if maze[vertical_i][horizontal_i] == 1:
        print('探索成功')
        print(depth)
        # exit()

    maze[vertical_i][horizontal_i] = 2

    print('移動後: ', vertical_i, horizontal_i)

    # 移動順は下→上→左→右
    if maze[vertical_i - 1][horizontal_i] < 2:
        search(vertical_i - 1, horizontal_i, depth + 1)
    if maze[vertical_i + 1][horizontal_i] < 2:
        search(vertical_i + 1, horizontal_i, depth + 1)
    if maze[vertical_i][horizontal_i - 1] < 2:
        search(vertical_i, horizontal_i - 1, depth + 1)
    if maze[vertical_i][horizontal_i + 1] < 2:
        search(vertical_i, horizontal_i + 1, depth + 1)

    print('探索失敗: ', vertical_i, horizontal_i)

    maze[vertical_i][horizontal_i] = 0


search(1, 1, 0)
