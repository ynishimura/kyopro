L = int(input())
M = int(input())
N = int(input())

sum_L = L * 100
sum_M = M * 25
sum_N = N * 1

sum = sum_L + sum_M + sum_N

count = 0

# 1000札は足さない
sum = divmod(sum, 1000)[1]

# 100
count += divmod(sum, 100)[0]
sum = divmod(sum, 100)[1]
# 25
count += divmod(sum, 25)[0]
sum = divmod(sum, 25)[1]
# 1
count += divmod(sum, 1)[0]
sum = divmod(sum, 1)[1]
print(count)
