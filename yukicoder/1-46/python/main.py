import math

first = input()
split_first = first.split()
A = int(split_first[0])
B = int(split_first[1])
# 123456789 987654321 => 9
# 切り上げなのでceil
print(math.ceil(B/A))
