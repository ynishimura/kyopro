N = int(input()) # 寿司の数
V = list(map(int, input().split())) # 寿司の美味しさ(半角スペース区切り)

score_list = [0] * (N+1)

def sushi_score():
    # 寿司が1つのとき
    if N == 1 :
        return V[0]

    '''
    # 1 2 3 4
    美味しさ最大になるとき
    3皿目が流れてきたとき
        3皿目の寿司を取ったとき
            4 = 1 + 3
            3皿までの美味しさ = (1皿までの美味しさ) + 3皿目の美味しさ(V3)
            連続でとれないので、3皿までの美味しさ = 4皿までの美味しさ
        3皿目を取らないとき
            3皿までの美味しさ = 2皿までの美味しさ
            4皿目までの美味しさが決まる
                6 = 2 + 4
                4皿までの美味しさ=2皿までの美味しさ + 4皿目の美味しさ
        => 4皿目までの美味しさが求めれる
        4皿までの美味しさ = 3皿までの美味しさ、2皿までの美味しさ+4皿目の美味しさの大きい方
    '''

    # 2皿目の美味しさ初期値
    score_list[1] = V[0]
    for i in range(2, N + 1):
        score_list[i] = max(score_list[i-1], score_list[i-2] + V[i-1])
        # print(score_list)
    return max(score_list)


if __name__ == "__main__":
    print(sushi_score())