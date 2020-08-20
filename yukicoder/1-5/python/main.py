L = int(input())
N = int(input())
W = list(map(int, input().split()))

W.sort()

count = 0
sum = 0

for w in W:
    if sum + w > L:
        break
    count += 1
    sum += w

print(count)
