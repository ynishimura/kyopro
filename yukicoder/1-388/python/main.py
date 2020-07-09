import math
S, F = map(int, input().split())

# 端数は切り捨て
print(math.floor((S/F) + 1))
