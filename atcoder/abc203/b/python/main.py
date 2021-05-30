N,K  = map(int, input().split())

num = 0

for n in range(N):
    for k in range(K):
        room = f'{n + 1}0{k + 1}'
        num += int(room)
        # print(f'{n + 1}0{k + 1}')

print(num)