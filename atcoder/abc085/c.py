N, Y = map(int, input().split())
# a+b+c=N
# a, b が決まれば、c=N−a−b と自動的に決まる。
for a in range(N+1):
    for b in range(N+1-a):
        c = N-a-b
        if a*10000+b*5000+c*1000 == Y:
            print(a, b, c)
            exit()
print(-1, -1, -1)
