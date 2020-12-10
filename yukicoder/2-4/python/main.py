import sys

N = int(input()) # おもりの数
weight_list = list(map(int, input().split())) # おもりの重さ(半角スペース区切り)

weight_sum = sum(weight_list)
half = weight_sum // 2
# possibleかimpossibleを返すだけなので、重さを気にする必要ない
# 全てのおもりを使って天秤が水平 => 片方に全重さ/2となるか判定
# おもり(100以下の重さのおもりが100個以下)

def check():
    if weight_sum % 2 != 0: # おもりの重さの合計が奇数のときimpossible
        print("impossible")
        sys.exit(0) # 終了
    else:
        '''
        # ex) 1 2 3
        # 重りの合計/2 = 3
        # 縦(重りの数)i x 横(重りの合計/2)j
        [[True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False]]
         
        #dp[重りの数(i)][(重りの合計/2)までの数字(j)] : i番目まで見た時に重さjを作ることができるか判定していく

        '''
        dp = [[True] + [False]*(half + 1) for i in range(N)] # 最初はTrue,
        for i in range(N):
            for j in range(half + 1):
                # dp[i番目までのおもりを見た時][左側の重さj]
                # i番目のおもりの時に,左側の重さがjが存在するか判定
                # j - weight_list[i]
                # 重りの合計/2(j) から 対象の重りの重さ(weight_list[i])　を　引く

                if dp[i-1][j]: # 一つ前の判定でTrue
                    dp[i][j] = True # 組み合わせが存在する
                    continue
                if j - weight_list[i] < 0: # 作りたい重さよりおもりが重い => 作れない
                    # omori_now = weight_list[i]
                    # omori_sum_yoko = j
                    # omori_kazu_tate = i
                    continue
                if dp[i-1][j - weight_list[i]]: # 作りたい重さで足りなかった分の重さは作れるか
                    # omori_now = weight_list[i]
                    # omori_sum_yoko = j
                    # omori_kazu_tate = i
                    dp[i][j] = True

    if dp[-1][weight_sum//2]:
        print('possible')
    else:
        print('impossible')


if __name__ == "__main__":
    check()