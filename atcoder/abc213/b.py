import copy

n = int(input())
a = list(map(int, input().split()))

b = copy.deepcopy(a)

b.sort()

print(a.index(b[-2]) + 1)
