N = input()

"""
はじめの数字と最後の数字を比べる
if 同じなら、次の数字を比べる
else 先頭に0を追加する

これを桁数の半分まで繰り返す

"""
# print(f'first: {first}, last: {last}, digit: {digit}, for: {int(digit / 2)}')


def check(N):
    check_cnt = 0
    while len(N) < 20:
        first = 0
        last = -1
        for i in range(int(len(N) / 2)):
            if (N[first] != N[last]):
                check_cnt = 0
                break

            else:
                first += 1
                last += -1
                check_cnt += 1
                if(int(len(N)/2) == check_cnt):
                    return 'Yes'

        N = f'0{N}'
    return 'No'


print(check(N))
