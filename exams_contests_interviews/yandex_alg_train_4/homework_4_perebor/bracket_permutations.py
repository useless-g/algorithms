s = []
open_brackets = []


def brackets_permutation(n, s="", open_round=0, open_square=0, close_round=0, close_square=0):
    if open_round + open_square + close_round + close_square == n:
        print(s)
        return
    end = n // 2
    if open_round + open_square < end:
        open_brackets.append(0)
        brackets_permutation(n, s + "(", open_round + 1, open_square, close_round, close_square)
        open_brackets.pop()
        open_brackets.append(1)
        brackets_permutation(n, s + "[", open_round, open_square + 1, close_round, close_square)
        open_brackets.pop()
    if open_brackets:
        if open_brackets[-1] == 0:
            if close_round < open_round:
                bruh = open_brackets.pop()
                brackets_permutation(n, s + ")", open_round, open_square, close_round + 1, close_square)
                open_brackets.append(bruh)
        else:
            if close_square < open_square:
                bruh = open_brackets.pop()
                brackets_permutation(n, s + "]", open_round, open_square, close_round, close_square + 1)
                open_brackets.append(bruh)


n = int(input())
if n % 2:
    print()
else:
    brackets_permutation(n)