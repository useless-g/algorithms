from collections import deque
import os


def read_reverse():
    with open("input.txt", "r") as f:
        f.seek(0, os.SEEK_END)
        position = f.tell()
        while position >= 0:
            f.seek(position)
            next_char = f.read(1)
            if next_char in ('(', ')'):
                yield position, next_char
            position -= 1


# dict?
len_a = 0
a = deque()
stack_trash = 0
for char in read_reverse():

    if len_a and char[1] == '(' and a[0][1] == ')':
        j = 0
        while j < len_a and a[j][1] == ')':
            j += 1
        j -= 1
        del a[j]
        len_a -= 1

    else:
        if char[1] == '(':
            stack_trash += 1
            if stack_trash > 1:
                len_a = 0
                break
        len_a += 1
        a.appendleft(char)


if len_a == 1:
    print(a[0][0]+1)
else:
    print(-1)
