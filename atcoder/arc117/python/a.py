a, b = map(int, input().split())

print(a+b)

"""
a個の正の整数を作成
1
b個の負の整数を作成
-1
[1, -1]
"""

res = []
if(a == b):
    for i in range(1, a+1):
        res.append(i)
        res.append(-i)
elif(a > b):
    res.extend(range(1, a+1))
    for i in range(1, b+1):
        if(i == b):
            res.append(-sum(res))
        else:
            res.append(-i)
elif(b > a):
    res.extend(range(-1, -(b+1), -1))
    for i in range(1, a+1):
        if(i == a):
            res.append(-sum(res))
        else:
            res.append(i)

print(*res)
