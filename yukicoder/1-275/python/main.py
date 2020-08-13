import numpy as np

N = int(input().strip())
L = list(map(int, input().split()))

L.sort()
data = np.array(L)
median = np.median(data)
print(median)
