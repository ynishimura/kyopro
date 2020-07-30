A, B = map(int, input().split())

for i in range(A, B+1):
    if (i % 3 == 0) or "3" in str(i):
        print(i)
