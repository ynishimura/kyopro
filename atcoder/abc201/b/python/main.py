N = int(input())
st = [input().split() for _ in range(N)]
st_dict = dict(st)
print(st_dict)
for key in st_dict:
    st_dict[key] = int(st_dict[key])
st_sorted = sorted(st_dict.items(), key=lambda x:x[1])
print(st_sorted[-2][0])
