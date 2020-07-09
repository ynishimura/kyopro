# 4/22 => 4 = 2 + 2
# X/Y => X = Y = HAPPY DAY
# 12/3 => 12 not= 0 + 3

import math

count = 0
for m in range(1, 13):
    for d in range(1, 32):
        if m == 2 and d == 29:
            break
        if m == 4 and d == 30:
            break
        if m == 6 and d == 30:
            break
        if m == 9 and d == 30:
            break
        if m == 11 and d == 30:
            break
        d10 = math.floor(d/10)
        d1 = d % 10
        if m == d10 + d1:
            # print('{}/{} => HAPPY DAY'.format(m, d))
            count += 1

print(count)
