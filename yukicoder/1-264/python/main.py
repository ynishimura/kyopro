jibun, aite = map(int, input().split())
# print(jibun, aite)

if jibun == aite:
    print('Drew')
elif (jibun + 1) % 3 == aite:
    print('Won')
else:
    print('Lost')
