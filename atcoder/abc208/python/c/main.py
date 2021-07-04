import copy
N, K = map(int, input().split())
A = list(map(int, input().split()))

B = copy.copy(A)
B.sort()


quotient = K // N
surplus = K % N
limit = B[surplus]

for i in range(N):
    if A[i] < limit:
        print(quotient+1)
    else:
        print(quotient)
