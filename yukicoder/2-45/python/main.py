N = int(input())
V = list(map(int, input().split()))

# 2連続で皿を取ることが出来ない
# 自分の前を過ぎたお寿司も取ることが出来ない

score_list = [0] * (N+1)

def sushi_score():
    # 寿司が一つのとき
    if N == 1:
        score_list[0] = V[0]
        return score_list[0]

    # 寿司が2つのとき
    if N == 2:
        score_list[1] = V[1]
        return score_list[1]

    for i in range(N):
        print(V, i, N)
        if (i + 2 == N):
            break
        score_list[i] = V[i] + V[i + 2]
        print(score_list)
    return max(score_list)


if __name__ == "__main__":
    print(sushi_score())