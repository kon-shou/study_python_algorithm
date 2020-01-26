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
    [1, 0],   # 下
    [0, 1],   # 右
    [-1, 0],  # 上
    [0, -1],  # 左
]

# 最初は下を向いている
vertical_i, horizontal_i, depth, facing_direction = 1, 1, 0, 0

while maze[vertical_i][horizontal_i] != 1:
    maze[vertical_i][horizontal_i] = 2

    print('現在地: ', vertical_i, horizontal_i)
    print('向いてる方向: ', facing_direction)

    # 「現在向いている方向」を基準に、右手→正面→左手→背面の順に、進めるかを試行する
    for next_direction, dir_value in enumerate([
        dir[(facing_direction - 1) % 4],  # 右手
        dir[facing_direction],            # 正面
        dir[(facing_direction + 1) % 4],  # 左手
        dir[(facing_direction + 2) % 4]   # 背面
    ]):
        if maze[vertical_i + dir_value[0]][horizontal_i + dir_value[1]] < 2:
            vertical_i += dir_value[0]
            horizontal_i += dir_value[1]
            # 進んだ歩数から、移動後に向いてる方向を求める
            facing_direction = dir.index(dir_value)
            depth += 1
            break
        # 移動できない and 既に移動した場所が存在する場合、移動した場所に戻る
        elif maze[vertical_i + dir_value[0]][horizontal_i + dir_value[1]] == 2:
            vertical_i += dir_value[0]
            horizontal_i += dir_value[1]
            facing_direction = dir.index(dir_value)
            depth -= 1
            break

print(depth)
