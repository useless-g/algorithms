def merge(a: list, b: list):
    i = j = 0
    c = [0 for _ in range(len(a) + len(b))]
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:  # "<=" means stable sort
            c[i+j] = a[i]
            i += 1
        else:
            c[i+j] = b[j]
            j += 1
    while i < len(a):
        c[i+j] = a[i]
        i += 1
    while j < len(b):
        c[i+j] = b[j]
        j += 1
    return c


if __name__ == "__main__":
    n = int(input())
    s = input()
    if n != 0:
        a = list(map(int, s.split()))
    else:
        a = []

    n = int(input())
    if n != 0:
        s = input()
        b = list(map(int, s.split(" ")))
    else:
        b = []

    print(" ".join(list(map(str, merge(a, b)))))
