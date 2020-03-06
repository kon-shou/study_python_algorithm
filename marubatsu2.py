goal = [
    0b111000000, 0b000111000, 0b000000111, 0b100100100,
    0b010010010, 0b001001001, 0b100010001, 0b001010100
]


# 勝ち負けの判定
def check(player):
    for mask in goal:
        if player & mask == mask:
            return True
    return False


# 評価値を算出する
def minimax(p1, p2, p2_turn):
    if check(p2):
        if p2_turn:
            return 1
        else:
            return -1

    board = p1 | p2
    if board == 0b111111111:
        return 0

    # 盤面でまだ埋まってないものを配列にする
    w = [i for i in range(9) if (board & (1 << i)) == 0]

    if p2_turn:
        return min([minimax(p2, p1 | (1 << i), not p2_turn) for i in w])
    else:
        return max([minimax(p2, p1 | (1 << i), not p2_turn) for i in w])


# 第１引数のp1の手番であるという前提
def play(p1, p2, turn):
    # 相手の結果が条件を満たすか確認する
    if check(p2):
        print('勝ち: ' + bin(p2))
        print('負け: ' + bin(p1))
        print('盤面: ' + bin(p1 | p2))
        return

    board = p1 | p2
    # print('盤面: ' + bin(board))
    if board == 0b111111111:
        print('引き分け: ' + bin(p2))
        print('引き分け: ' + bin(p1))
        print('盤面: ' + bin(p1 | p2))
        return

    # 盤面でまだ埋まってないものを配列にする
    w = [i for i in range(9) if (board & (1 << i)) == 0]
    print('候補: ' + str(w))
    r = [minimax(p2, p1 | (1 << i), True) for i in w]
    print('期待値:' + str(r))
    j = w[r.index(max(r))]
    print('実際の値:' + str(j))
    play(p2, p1 | (1 << j), not turn)


play(0, 0, True)
