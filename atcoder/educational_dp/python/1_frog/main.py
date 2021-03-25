N = int(input()) # N個の足場
H = list(map(int, input().split())) # 足場の高さ
dp = [float('inf') for _ in range(N)] # DPテーブル
dp[0] = 0 # 最初のコスト
dp[1] = abs(H[0] - H[1])
for i in range(2, N):
  one_step = dp[i-1] + abs(H[i] - H[i-1])
  two_step = dp[i-2] + abs(H[i] - H[i-2])
  dp[i] = min(one_step, two_step)
print(dp[-1]) #最後の値が求めたいコスト