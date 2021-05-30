"""
https://atcoder.jp/contests/abc203/tasks/abc203_a
"""

list  = list(map(int, input().split()))

a = [x for x in set(list) if list.count(x) != 2]
if len(a) >= 3:
    print(0)
else:
    print(int(a[0]))