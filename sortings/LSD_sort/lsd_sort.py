n = int(input())

a = [input() for _ in range(n)]
print("Initial array:")
print(", ".join(a))
print("**********")
for phase in range(1, len(a[0]) + 1):
    buckets = {str(i): [] for i in range(10)}
    for s in a:
        buckets[s[-phase]].append(s)
    print(f"Phase {phase}")
    a = []
    for key, value in buckets.items():
        print(f"Bucket {key}: {', '.join(value) if value else 'empty'}")
        a += value
    print("**********")

print("Sorted array:")
print(", ".join(a))
