"""
https://atcoder.jp/contests/abc203/tasks/abc203_c

N K
2 3
---
2 1
5 10

村の移動コストは+1なので、
村のK(3)番目までは必ずいける

回復するところのNを見て、
Kより小さいところは回復できる
3 > 2なので所持金+1される

5は3+1より小さいので、+10されない

村の移動コストは+1なので、
Kの値がそのまま、いける村の数になる

ただし、回復できるか判断するためにソートする必要がある

下記の場合
N K
3 2
---
5 5
2 1
2 2

K = 2なので、Nが2のところで回復できる
K = 2 + 1 + 2
=> 5
これが5に達するので、N=5で+5される
つまり、K=10になり、村10までいける

"""

N,K  = map(int, input().split())

num_list = [list(map(int, input().split())) for _ in range(N)]

# print(num_list)

li = sorted(num_list, key=lambda x: x[0])

#print(li)

for i in li:
    if i[0] <= K:
        #print(i[0])
        K += i[1]

print(K)

## 下記のやり方は計算量が多くなりすぎる
# vil = 0
# while K >= 0:

#     #print(f'村{vil}')
#     #print(f'所持金{K}')
    
#     for i in num_list:
#         if i[0] == vil:
#             print(f'回復 +{i[1]}')
#             K += i[1]
    
#     vil += 1
#     K -= 1
# print(vil)