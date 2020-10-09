from collections import deque
N = int(input())


def movable_distance(num):
    "2進数で表現した時の1のビット数 => 前後に移動できる距離"
    # print(f'num:{num}, b:{bin(num)}')
    # 2進数表示した場合の1の数を数える
    return bin(num).count("1")


def bit():
    que = deque()
    que.append(1)  #探索するマス
    # マスの数を表す整数N(1<N<10000)が与えられます。
    trout = deque([0] * (N + 1))

    # 1から開始のマス
    trout[1] = 1

    while (len(que) > 0):
        # print(f'#### {que}')
        now = que.popleft()  #現在のマス目

        # debug
        # for i in range(N):
        #     if (i + 1 == now):
        #         print(f'*{trout[i + 1]}|', end='')  #現在のマス目
        #     elif (now == N):
        #         print(f'gaol => {trout[now]}', end='')  #終了
        #         break
        #     elif (trout[i + 1] != 0):
        #         print(f'{trout[i + 1]}|', end='')  #探索済マス
        #     else:
        #         print('-|', end='')  #未探索マス
        # print()

        if now == N:
            return trout[N]  #目的の最小移動数

        movecnt = movable_distance(now)  #現在のマス目を２進数に変換した時の1の数
        # print(f'now {now}, movecnt {movecnt}')

        back = now - movecnt  #後ろのマスに移動する
        forward = now + movecnt  #前のマスに移動する

        if (back > 0 and trout[back] == 0):
            que.append(back)  #探索を行うためキューに入れる
            trout[back] = trout[now] + 1  #移動した先に移動数の最小値を記録
            # print(
            #     f'マス{back}への移動数の最小値を記録: {trout[back]}, 探索を行うための位置をappend: {back}'
            # )

        if (forward <= N and trout[forward] == 0):
            que.append(forward)  #探索を行うためキューに入れる
            trout[forward] = trout[now] + 1  #移動した先に移動数の最小値を記録
            # print(
            #     f'マス{forward}への移動数の最小値を記録: {trout[forward]}, 探索を行うための位置をappend: {forward}'
            # )

    return -1


if __name__ == "__main__":
    print(bit())
