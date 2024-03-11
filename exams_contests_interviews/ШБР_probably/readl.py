import os
import sys
from collections import deque
def read_reverse():
    with open("input.txt", "r") as f:
        f.seek(0, os.SEEK_END)
        position = f.tell()
        while position >= 0:
            f.seek(position)
            next_char = f.read(1)
            if next_char == '(':
                yield position, ')'
            elif next_char == ')':
                yield position, '('
            position -= 1


for i in read_reverse():
    print(i, end='')
a = deque([1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,1])
b = list([1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,11,1,1,1,1,11,1,1,1,1])
print(sys.getsizeof(a), sys.getsizeof(b))