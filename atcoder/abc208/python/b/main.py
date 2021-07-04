import math

p = int(input())
N = 10
# INF = 10**10
# C = [math.factorial(i) for i in range(N+1)]
# dp = [[INF]*(p+1) for _ in range(N+1)]

# dp[0][0] = 0
# for m in range(N):
#     for n in range(p+1):
#         if n-C[m] >= 0:
#             dp[m+1][n] = min(dp[m+1][n-C[m]]+1, dp[m][n])
#         else:
#             dp[m+1][n] = dp[m][n]
# print(dp[N][p])

count = 0
while True:
    if p >= math.factorial(N):
        p = p - (math.factorial(N))
        count += 1
    elif p == 0:
        print(count)
        break
    else:
        N -= 1
