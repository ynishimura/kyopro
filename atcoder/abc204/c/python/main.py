import sys
N, M = map(int,input().split()) 
a = [list(map(int, input().split())) for _ in range(M)]

"""
3 3
1 2
2 3
3 2

N=3
M=3
3個の都市、3個の道路
A => B OK
B => A NG

条件
Mが0のとき、N通り

N*Mから引いていくのが良さそう


"""

# print(a)

L = list(map(list, (zip(*a))))

total = []
if M == 0:
    print(N)
    sys.exit()
A = L[0]
A.sort()
B = L[1]
B.sort()
if A == B:
    print(f'ok, {A} : {B}')
    print(len(L[0]) ** 2)
else:
    result = list(set(L[0]) - set(L[1]))
    setL1 = set(L[1])
    print((len(L[0]) ** 2) - (len(set(result)) * len(setL1)))

# for i in L[0]:
#     total.append((i,i)) 
#     for j in L[1]:
#         total.append((i,j))
        
# print(set(total))    
# print(len(set(total)))    