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

pos = [
    [1, 1, 0]
]

while len(pos) > 0:
    vertical_i, horizontal_i, depth = pos.pop(0)

    if maze[vertical_i][horizontal_i] == 1:
        print(depth)
        break

    maze[vertical_i][horizontal_i] = 2

    if maze[vertical_i - 1][horizontal_i] < 2:
        pos.append([vertical_i - 1, horizontal_i, depth + 1])
    if maze[vertical_i + 1][horizontal_i] < 2:
        pos.append([vertical_i + 1, horizontal_i, depth + 1])
    if maze[vertical_i][horizontal_i - 1] < 2:
        pos.append([vertical_i, horizontal_i - 1, depth + 1])
    if maze[vertical_i][horizontal_i + 1] < 2:
        pos.append([vertical_i, horizontal_i + 1, depth + 1])

    print('pos')
    print(pos)
