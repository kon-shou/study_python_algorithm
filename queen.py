N = 8


# 斜めのチェック
def can_place(x, col):
    # 配置済みの行を逆順に調べる
    for i, row in enumerate(reversed(col)):
        if (x + i + 1 == row) or (x - i - 1 == row):
            return False
    return True


def search(col):
    if len(col) == N:
        print(col)
        return

    for i in range(N):
        # colは０〜７までのx座標を格納した配列
        # 既に同一のx座標が格納されていたら、つぎのx座標を確認する
        if i in col:
            continue

        if can_place(i, col):
            col.append(i)
            search(col)
            col.pop()


search([])
