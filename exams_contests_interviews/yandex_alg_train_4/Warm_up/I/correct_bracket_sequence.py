s = input()
stack = []
opened = "(", "[", "{"
closed = ")", "]", "}"
for i in s:
    if stack and (stack[-1] in opened) and (i in closed) and (opened.index(stack[-1]) == closed.index(i)):
        stack.pop()
    else:
        stack.append(i)

print("no" if stack else "yes")
