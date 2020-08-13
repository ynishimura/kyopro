K, N, F = map(int, input().split())
A = list(map(int, input().split()))

sum = K * N

for age in A:
    sum -= age

if (sum < 0):
    print(-1)
else:
    print(sum)
