from typing import List


h, w, n = map(int, input().split())

num_list = []

for i in range(n):
    num_list.append(list(map(int, input().split())))

print(num_list)

for idx_i, i in enumerate(range(h)):
    print("*", end="")
    for idx_j, j in enumerate(range(w)):
        if idx_i == 3 and idx_j == 2:
            print("1", end="")
        else:
            print("*", end="")
    print()
