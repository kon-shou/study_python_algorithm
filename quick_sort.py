data = [6, 15, 4, 2, 2, 2, 8, 5, 11, 9, 9, 9, 15, 7, 13]


def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left, right, same = [], [], 0

    for i in data[1]:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            same += 1

    print('pivot')
    print(pivot)
    print('before_left')
    print(left)
    print('before_right')
    print(right)

    left = quick_sort(left)

    print('after_left')
    print(left)

    right = quick_sort(right)

    print('after_right')
    print(right)

    return left + [pivot] + right


print(quick_sort(data))
