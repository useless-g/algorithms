from json import loads, dumps
import datetime


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


goods_list = loads(input())
for q in range(5):
    s = input().split(' ')
    if s[0] == 'NAME_CONTAINS':
        NAME_CONTAINS = s[1]
    elif s[0] == 'PRICE_GREATER_THAN':
        PRICE_GREATER_THAN = int(s[1])
    elif s[0] == 'PRICE_LESS_THAN':
        PRICE_LESS_THAN = int(s[1])
    elif s[0] == 'DATE_AFTER':
        DATE_AFTER = datetime.datetime.strptime(s[1], '%d.%M.%Y')
    elif s[0] == 'DATE_BEFORE':
        DATE_BEFORE = datetime.datetime.strptime(s[1], '%d.%M.%Y')

answer = []
for good in goods_list:
    if (PRICE_GREATER_THAN <= good['price'] <= PRICE_LESS_THAN
            and DATE_BEFORE >= datetime.datetime.strptime(good['date'], '%d.%M.%Y') >= DATE_AFTER
            and kmp(good['name'].lower(), NAME_CONTAINS.lower())):
        answer.append(good)

print(dumps(sorted(answer, key=lambda x: int(x["id"]))))
