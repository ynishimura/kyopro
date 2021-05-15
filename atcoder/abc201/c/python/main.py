# https://atcoder.jp/contests/abc201/submissions/22620837
S = input()

# xxxxx?xxxo
# 2 * 2 * 2 * 2 - (1)
# 15
# 5 5 5 5のときを引く


# ooo???xxxx
# 6 * 6 * 6 * 6 - ()
# 108
# 0 1 2 が入ってないとき

# o?oo?oxoxo
# 0

# 3 
o_count = 0

# 3
hatna_count = 0

x_count = 0
for i, word in enumerate(S):
    print(i, word)