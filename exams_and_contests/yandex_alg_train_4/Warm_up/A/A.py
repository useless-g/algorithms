N, M = tuple(map(int, input().split(" ")))
seq = list(map(int, input().split(" ")))
for _ in range(M):
	L, R = tuple(map(int, input().split(" ")))
	m = seq[L]
	for i in range(L + 1, R + 1):
		if seq[i] < m:
			m = seq[i]
	for i in range(L, R+1):
		if seq[i] != m:
			print(seq[i])
			break
	else:
		print("NOT FOUND")
