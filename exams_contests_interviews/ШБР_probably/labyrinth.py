def up(a, b):
    global arr
    a, b = a - 1, b
    c = 'U'
    return a, b, c


def down(a, b):
    global arr
    a, b = a + 1, b
    c = 'D'
    return a, b, c


def left(a, b):
    global arr
    a, b = a, b - 1
    c = 'L'
    return a, b, c


def right(a, b):
    global arr
    a, b = a, b + 1
    c = 'R'
    return a, b, c


def change_space(a, b, c):
    global arr, empty
    if arr[a][b] == '.':
        arr[a][b] = c
        empty -= 1


def print_labyrinth():
    global arr
    for k in arr:
        print(''.join(k))


n, m = tuple(map(int, input().split()))
arr = [list(input()) for i in range(n)]

empty = 0
Si = Sj = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '.':
            empty += 1
        elif arr[i][j] == 'S':
            Si = i
            Sj = j

i = Si
j = Sj
vector = (left, down, right, up)
vector_index = 0
while empty:

    ii, jj, char = vector[(vector_index + 1) % 4](i, j)
    if arr[ii][jj] != '#':
        i, j = ii, jj
        change_space(i, j, char)
        vector_index = (vector_index + 1) % 4

    else:
        ii, jj, char = vector[vector_index % 4](i, j)
        if arr[ii][jj] != '#':
            i, j = ii, jj
            change_space(i, j, char)
        else:
            ii, jj, char = vector[(vector_index - 1) % 4](i, j)
            if arr[ii][jj] != '#':
                i, j = ii, jj
                change_space(i, j, char)
                vector_index = (vector_index - 1) % 4
            else:
                ii, jj, char = vector[(vector_index - 2) % 4](i, j)
                if arr[ii][jj] != '#':
                    i, j = ii, jj
                    vector_index = (vector_index - 2) % 4


print_labyrinth()
