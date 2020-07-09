# 標準入力から一行分を読み出し、文字列として格納する。
first = input()

# 読み込んだ文字列をスペースで分割する
split_first = first.split()

# それぞれをint型に変換する
A = int(split_first[0])  # forの数
# B = int(split_first[1])

# 慣れてくると この一行でよい
# A, B = map(int, input().split())

# 参考: リストを読む際はlist()で覆ってやらないといけない
# L = list(map(int, input().split()))

# print(A, L)
# 2行目を読み込む
num = 0
for i in range(A):
    num += int(input())
print(num)
