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


def next_position(x, y, depth):
    if maze[y][x] == 1:
        print('x: ', str(x) + ', y: ',  str(y))
        print('深さ(=探索回数): ', str(depth))
        exit()

    maze[y][x] = 2
    next_positions = []
    if maze[y - 1][x] < 2:
        next_positions.append({'x': x, 'y': y - 1, 'depth': depth + 1})
    if maze[y + 1][x] < 2:
        next_positions.append({'x': x, 'y': y + 1, 'depth': depth + 1})
    if maze[y][x - 1] < 2:
        next_positions.append({'x': x - 1, 'y': y, 'depth': depth + 1})
    if maze[y][x + 1] < 2:
        next_positions.append({'x': x + 1, 'y': y, 'depth': depth + 1})

    return next_positions


def search(_positions):
    positions = []
    # flatten()する
    for sublist in _positions:
        if sublist is None:
            continue
        elif type(sublist) is dict:
            positions.append(sublist)
        else:
            for pos in sublist:
                positions.append(pos)

    print('postions: ' + str(positions))
    search([next_position(pos['x'], pos['y'], pos['depth']) for pos in positions])


if __name__ == '__main__':
    search([{'x': 1, 'y': 1, 'depth': 0}])
