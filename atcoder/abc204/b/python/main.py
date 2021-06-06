N = input().split()
l = list(map(int,input().split()))

total = 0
for i in l:
    if i > 10:
        total += i - 10
print(total)