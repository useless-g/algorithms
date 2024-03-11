import os


def read_reverse():
    with open("input.txt", "r") as f:
        f.seek(0, os.SEEK_END)
        position = f.tell()
        while position >= 0:
            f.seek(position)
            next_char = f.read(1)
            if next_char == '(':
                yield position, ')'
            if next_char == ')':
                yield position, '('
            position -= 1


braces = ('(', ')')
a = list()
stack_trash = 0
len_a = 0
for char in read_reverse():

    if len_a and char[1] == ')' and a[len_a - 1][1] == '(':
        j = 0
        while a[j][1] != '(':
            j += 1
        j -= 1
        len_a -= 1
        del a[j]

    else:
        len_a += 1
        a.append(char)
        # if char[1] == '(':
        #     stack_trash += 1
        #     if stack_trash > 1:
        #         a = []
        #         break

if len_a == 1:
    print(a[0][0] + 1)
else:
    print(-1)
