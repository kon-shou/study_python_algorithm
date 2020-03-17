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

dir = [
    {'x': 0, 'y': 1},  # 下
    {'x': 1, 'y': 0},  # 右
    {'x': 0, 'y': -1},  # 上
    {'x': -1, 'y': 0},  # 左
]

x, y, depth = 1, 1, 0
# 最初は下を向いている
facing_direction = 0

while maze[y][x] != 1:
    maze[y][x] = 2

    print('現在地 x:' + str(x) + ' y:' + str(y))
    if facing_direction == 0:
        print('向いてる方向: 下')
    elif facing_direction == 1:
        print('向いてる方向: 右')
    elif facing_direction == 2:
        print('向いてる方向: 上')
    elif facing_direction == 3:
        print('向いてる方向: 左')

    # 「現在向いている方向」を基準に、右手→正面→左手→背面の順に、進めるかを試行する
    for _, dir_value in enumerate([
        dir[(facing_direction - 1) % 4],  # 右手
        dir[facing_direction],            # 正面
        dir[(facing_direction + 1) % 4],  # 左手
        dir[(facing_direction + 2) % 4]   # 背面
    ]):
        if maze[y + dir_value['y']][x + dir_value['x']] < 2:
            y += dir_value['y']
            x += dir_value['x']
            # 進んだ歩数から、移動後に向いてる方向を求める
            facing_direction = dir.index(dir_value)
            depth += 1
            break
        # 移動できない and 既に移動した場所が存在する場合、移動した場所に戻る
        elif maze[y + dir_value['y']][x + dir_value['x']] == 2:
            y += dir_value['y']
            x += dir_value['x']
            facing_direction = dir.index(dir_value)
            depth -= 1
            break

print(depth)
