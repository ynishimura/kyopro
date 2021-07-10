N, X = map(int, input().split())
A = list(map(int, input().split()))

item = N
syojikin = X
nedan = A

total = 0
for i in A:
    total += i
waribiki = item // 2

need = total - waribiki

if syojikin >= need:
    print("Yes")
else:
    print("No")
