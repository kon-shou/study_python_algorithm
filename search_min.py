data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

min_index = 0
for i in range(1, len(data)):
    if data[min_index] > data[i]:
        min_index = i

print(min_index)
