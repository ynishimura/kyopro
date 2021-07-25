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
# for c in s:
#     for i in range(9):
#         if chokudai[i] == c:
#             dp[i] += dp[i-1]
#             dp[i] %= MOD

# print(dp[-1])
