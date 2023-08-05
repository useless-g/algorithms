# Complete the alternate function below.
def alternate(s):
    if len(s) < 2:
        return 0
    alf = "abcdefghijklmnopqrstuvwxyz"
    maxim = 0
    for i in range(len(alf) - 1):
        for j in range(i + 1, len(alf)):
            s2 = list(s)
            for k in s:
                if k != alf[i] and k != alf[j]:
                    s2.remove(k)
            for k in range(len(s2) - 1):
                if s2[k] == s2[k + 1]:
                    s2 = ''
                    break
            maxim = max(maxim, len(s2))

    return maxim

