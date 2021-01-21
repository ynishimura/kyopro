"""
https://yukicoder.me/problems/209
問題
ここに0番〜(N-1)番の品物がある。
また、
item1 item2 score
という形式で書かれた得点表がある。
品物を並べた時、item1がitem2よりも前であればscore点を獲得できるという意味である。

得点表が与えられるので、品物を適切に並び替えた時、獲得できる得点を最大化したい。そのときの得点を出力せよ。

注意：LL系の言語だと工夫しないといけないかもしれません。

---
https://note.nkmk.me/python-math-factorial-permutations-combinations/
リストから順列を生成、列挙: itertools.permutations()
総数だけでなく、リスト（配列）などから順列を生成して列挙することも可能。
第一引数にイテラブル（リストや集合set型）、第二引数に選択する個数を渡すと、その順列のイテレータを返す。
"""

import itertools

# 入力
(n, m) = [int(i) for i in input().rstrip().split()]

table = []
for i in range(n):
    table += [[0] * n]

# 各行読み込む
for i in range(m):
    item1, item2, score = [int(x) for x in input().split()]
    # スコア表作成
    table[item1][item2] = score

max_score = 0
# 得点計算
for v in itertools.permutations(range(n)): #順列を生成する
    score = 0
    for i in range(1, len(v)):
        for j in range(0, i):
            # スコア表に沿って得点を追加していく
            score += table[v[j]][v[i]]
    # 比較して大きい得点を格納
    max_score = max(score, max_score)

print(max_score)