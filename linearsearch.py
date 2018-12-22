#Challenge : Linear search

pos = -1

def search(lists, n):

    for i in range(len(lists)):
        if lists[i] == n:
            globals() ['pos'] = i
            return True

    return False


lists = [5, 8, 4, 6, 9, 2]
n = 4

if search(lists, n):
    print("Found at", pos)
else:
    print("not found")
