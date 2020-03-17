X, Y = 6, 5

# 交点を通るパターンを、縦列を左端から順番に、全て０の配列にする
route = [[0 for _ in range(Y + 1)] for _ in range(X + 1)]

# 最下段の行を、全て１とする
for i in range(X + 1):
    # 左端の列の最下段は０
    route[i][0] = 0 if i == 0 else 1

print(route)

for y in range(1, Y + 1):
    # 左端の列の、下からy番目を１とする
    route[0][y] = 1

    for x in range(1, X + 1):
        # 左と下から加算する
        route[x][y] = route[x - 1][y] + route[x][y - 1]
        print(route)

print(route[X][Y])
