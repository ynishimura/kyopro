N, A, X, Y = map(int, input().split())

total = 0
if N > A:
    total += A * X
    total += (N-A) * Y
elif N < A:
    total += N * X
else:
    total += A * X

print(total)
