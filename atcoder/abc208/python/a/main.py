a, b = map(int, input().split())

if (b > 600):
    print("No")
elif (a > b):
    print("No")
elif (a * 6) >= b:
    print("Yes")
else:
    print("No")
