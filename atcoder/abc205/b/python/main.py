import sys
N = int(input())
A = list(map(int, input().split()))

A.sort()

for i,v in enumerate(A):
    if i+1 != v:
       print('No')
       sys.exit()

print('Yes')