X = int(input())
Y = int(input())
L = int(input())


turn = 0
forward_x = abs(int(X / L))
forward_y = abs(int(Y / L))

if Y >= 0:
    if X == 0:
        turn = 0
    else:
        turn = 1
else:
    turn = 2

# ちょっと残るときは+1しておく
if not X % L == 0:
    forward_x += 1
if not Y % L == 0:
    forward_y += 1

print(forward_x + forward_y + turn)
