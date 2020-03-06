def hanoi(n, src, dist, via):
    print(str(n))
    if n > 1:
        # 一番下を残して、それ以外を via に移す
        hanoi(n - 1, src, via, dist)
        # 一番下を dist に移す
        print(str(n) + '一番下の移動: ' + src + '->' + dist)
        # via にある塔を dist に移す
        hanoi(n - 1, via, dist, src)
    # 塔がひとつだけの場合、無条件で dist へ移動させる
    else:
        print(str(n) + '塔が一つの移動: ' + src + '->' + dist)


hanoi(int(input()), '出発地', '目的地', '経由地')
