import sys
a,b,c = map(int, input().split())

if (c % 2) != 0: 
    if a == b:
        print('=')
        sys.exit()

    if a > b:
        print('>')
        sys.exit()

    if a < b:
        print('<')
        sys.exit()
else:
    if abs(a) == abs(b):
        print('=')
        sys.exit()

    if abs(a) > abs(b):
        print('>')
        sys.exit()

    if abs(a) < abs(b):
        print('<')
        sys.exit()