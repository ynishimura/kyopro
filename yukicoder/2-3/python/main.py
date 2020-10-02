# N = int(input())

# bin_num = bin(N)

# print(bin_num)

# # 移動可能回数
# # Qにはその位置から移動できる場所を入れる
# # - 前に移動したとき
# # - 後に移動したとき
# queue =

# # 移動した回数を保存
# count =

# # 動したか、していないかを保存
# move =

from collections import deque
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1
grid = [input() for _ in range(r)]

# print(grid)
q = deque()
q.append((sy, sx))

INF = '#'  #1<<60 # 2: 0001 1<<3: 1000
dist = [[INF for _ in range(c)] for __ in range(r)]
dist[sy][sx] = 0

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

while (len(q) > 0):
    now = q.popleft()
    y, x = now

    for di in range(4):
        ny = y + dy[di]
        nx = x + dx[di]

        if (ny < 0 or ny >= r or nx < 0 or nx >= c): continue
        if (grid[ny][nx] == '#'): continue
        if (dist[ny][nx] != INF): continue

        dist[ny][nx] = dist[y][x] + 1
        q.append((ny, nx))

for i in range(r):
    for j in range(c):
        print(dist[i][j], end='')
    print()

print(dist[gy][gx])