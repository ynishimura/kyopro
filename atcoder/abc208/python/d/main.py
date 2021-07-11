INF = 10 ** 10

N, M = map(int, input().split())

dp = [[INF] * N for _ in range(N)]


for i in range(N):
    dp[i][i] = 0

for i in range(M):
    a, b, c = map(int, input().split())
    dp[a-1][b-1] = c

Ans = 0

for k in range(N):
    for s in range(N):
        for t in range(N):
            dp[s][t] = min(dp[s][t], dp[s][k] + dp[k][t])
            if dp[s][t] != INF:
                Ans += dp[s][t]

print(Ans)
