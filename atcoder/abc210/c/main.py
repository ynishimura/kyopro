N, K = map(int, input().split())
C = list(map(int, input().split()))

max = len(set(C))
num = 0
i = 0

if N == K:
    print(max)
else:
    while K == len(C[i:K+i]):
        # for i in range(K+1):
        num = len(set(C[i:K+i]))

        if max == num:
            break

        # print(C[i:K+i])
        i += 1

    print(num)
"""
a[0:3] => a[0:K]
~
a[4:7] => a[K+1:N]

N = K + K +1


"""
