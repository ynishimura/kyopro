N = int(input())
N -= 1

"""
N=3
A:1,B:2
A:2,B:1
"""

ans = 0


while N >= 0:
    if N == 0:
        break
    else:
        ans += 1
        N -= 1

print(ans)
