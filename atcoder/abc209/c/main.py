"""
3 3 4 4 のとき

3-0 * 3-1 * (3-2)+1 * (3-3)+1
3   *  2  * 2       * 1
=> 12


3 2 4 4　のとき

3-0 * 2-1 * (3-2)+(4-3) * (3-3)+(4-3) 

3   * 1   *  2          * 1
=> 6

同じ数字はだめ
1 1 3 4

入力できる数字は入力された数字以下の数
３だったら

1
2
3


"""

N = int(input())
C = list(map(int, input().split()))
C.sort()
total = C[0]

for i in range(1, N):
    total *= (C[i] - i)
    total %= (10**9 + 7)

print(total)

# for idx, i in enumerate(C):
#     # print(idx, i, total)
#     if idx == 0:
#         continue

#     if base < C[idx]:
#         sabun = C[idx] - base
#         print(idx, sabun)
#         total *= (base - idx) + (C[idx] - base)
#     else:
#         total *= C[idx] - idx

# print(total % (10**9+7))
