import os

queue = ['/home/']

while len(queue) > 0:
    print(queue)
    dir = queue.pop()
    for i in os.listdir(dir):
        if i == 'book':
            print(dir + i)
            break
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):
                queue.append(dir + i + '/')
