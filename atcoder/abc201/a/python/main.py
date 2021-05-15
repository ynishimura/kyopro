list  = list(map(int, input().split()))
list.sort()
A1 = list[0]
A2 = list[1]
A3 = list[2]

if(A3 - A2 == A2 -A1):
    print('Yes')
else:
    print('No')