s1 = input()
s2 = input()
s3 = input()
s4 = input()

list = ['H', '2B', '3B', 'HR']
check = ['H', '2B', '3B', 'HR']


for i in list:
    if i == s1:
        check.remove(i)
        continue
    if i == s2:
        check.remove(i)
        continue
    if i == s3:
        check.remove(i)
        continue
    if i == s4:
        check.remove(i)
        continue

if len(check) > 0:
    print('No')
else:
    print('Yes')
