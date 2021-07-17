N = int(input())
S = input()

for idx, i in enumerate(S):
    if int(i) == 1:
        if (idx + 1) % 2 == 0:
            print('Aoki')
        else:
            print('Takahashi')
        break
