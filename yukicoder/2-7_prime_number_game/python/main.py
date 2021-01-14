import sys

# N = int(input())

"""
https://yukicoder.me/problems/25
問題
あなたと素数を習ったばかりのEveは、素数のゲームを思いついた。

ゲームの内容は以下のとおりです。
・まず初めに、先攻のプレイヤーに2以上の自然数Nが与えられます。
・その番のプレイヤーはNに対して、「N以下（Nも含む）の素数」のどれかで減算する、
その数をN'とすると、N'が0または1になってしまったら、そのプレイヤーの負けである。
・その後N'を新たなNとし、相手にその数を渡し、以上を繰り返します。

まずあなたが先攻となりゲームを始めます。
この時、どちらも負けないように動くと考える。自然数Nが与えられた時、
あなたが勝つことが出来る場合Win、それ以外はLoseを返してください。
"""


"""
N:2以上10000未満

素数:1を含めない,N以下の素数を使う

N - 素数 = N'
N' = 0 or 1 ==> Lose

先攻: You
後攻: Eve

---
入力:5 => Win
素数:[2, 3, 5]

縦:素数,
横:入力の数字の連番

「数字 - 総数」を判定してメモ
マイナスになるとき:-
loseになるとき:x
2以上になるとき:o
0,1のときはwin

 12345
2-xxo
3--xxo
5----x

---

入力:12 => Lose
素数:[2, 3, 5, 7, 11]
  1 2 3 4 5 6 7 8 9 10 11 12
2 - x x 2
3 - - x x 2
5 - - - - x x 2 3 4 
7 - - - - - - x x 2 3  4  5
11- - - - - - - - - -  x  x


"""

def eratosthenes(N):
    """素数を生成.
    エラトステネスの篩
    """
    L = [True] * (N + 1)

    for i in range(2, int(N ** 0.5) + 1):
        if L[i]:
            for j in range(i * 2, N, i):
                L[j] = False

    return [i for i, b in enumerate(L[2:], 2) if b]


def resolve(input):
    N = int(next(input))
    primes = eratosthenes(N)

    dp = [False] * (N + 1)
    dp[0] = True
    dp[1] = True

    for n in range(2, N + 1):
        for prime in primes:
            p = n - prime
            if p < 0:
                break
            if dp[p] is False:
                dp[n] = True
                break

    # print(dp)
    return 'Win' if dp[N] else 'Lose'


def main():
    ans = resolve(sys.stdin.buffer)
    print(ans)


if __name__ == '__main__':
    main()