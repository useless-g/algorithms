n = int(input())

for _ in range(n):
    start = input()
    finish = input()
    letters = dict()
    flag = True
    for i, j in zip(start, finish):
        if i != j:
            if letters.get(i):
                if letters[i] != j:
                    flag = False
                    break
            else:
                letters[i] = j

    if flag:
        if len(set(letters.keys())) != len(set(letters.values())):
            flag = False

    if flag:
        letters_keys = list(letters.keys())
        for letter in letters_keys:
            if letters.get(letters[letter]) and letter != letters[letters[letter]]:
                flag = False
                break

    print("YES" if flag else "NO")
