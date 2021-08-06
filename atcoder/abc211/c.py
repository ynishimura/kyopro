S = input()

target = "chokudai"

mod = 10**9 + 7

dp = [[0 for _ in range(len(target) + 1)] for _ in range(len(S) + 1)]

for i in range(len(S) + 1):
    dp[i][0] = 1

for j in range(len(target)):
    for i in range(len(S)):
        if S[i] == target[j]:
            dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % mod
        else:
            dp[i+1][j+1] = dp[i][j+1]

print(dp[len(S)][len(target)])
# s = input()
# t = "chokudai"
# m = len(t)
# dp = [0]*(m+1)
# dp[0] = 1
# for c in s:
# 	for i in range(m):
# 		if t[i] == c:
# 			dp[i+1] = (dp[i] + dp[i+1]) % (10**9+7)
# print(dp[-1])
