import os


def search(dir, name):
    print(dir)
    for i in os.listdir(dir):
        if i == name:
            print(dir + i)
            return
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):
                search(dir + i + '/', name)


search('/', 'book')
