from collections import Counter

def missingCharacters(s):
    d = Counter(s)
    answer = ""
    for digit in "0123456789":
        if not d.get(digit):
            answer += digit
    for char in "abcdefghijklmnopqrstuvwxyz":
        if not d.get(char):
            answer += char
    return answer
