def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2

        print('left')
        print(left)
        print('right')
        print(right)
        print('mid')
        print(mid)

        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(data, 40))
