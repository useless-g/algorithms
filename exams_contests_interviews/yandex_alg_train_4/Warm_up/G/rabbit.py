n, m = map(int, input().split(" "))
dp = [[0 for j in range(m+1)] for i in range(n+1)]
answer = 0
for i in range(1, n+1):
    s = list(map(int, input().split(" ")))
    for j in range(1, m+1):
        if s[j-1]:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
            answer = max(answer, dp[i][j])

print(answer)
