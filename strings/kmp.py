def prefix(string):
    p = [0] * len(string)
    i = 1
    j = 0
    while i < len(string):
        if string[j] == string[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]
    return p


def kmp(string, substring):
    p = prefix(substring)
    i = j = 0
    while i < len(string):
        if string[i] == substring[j]:
            i += 1
            j += 1
            if j == len(substring):
                return True
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1
    return False


print(kmp('лилили лилило лилилась', 'лилила'))
