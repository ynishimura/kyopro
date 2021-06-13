import math
a, b = map(int, input().split())


result = (b / 100) * a

f, i = math.modf(result)
print(f, i)
if f == 0:
    print(int(result))
else:
    print(result)