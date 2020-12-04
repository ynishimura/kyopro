N = int(input()) # おもりの数
Weight = list(map(int, input().split())) # おもりの重さ(半角スペース区切り)

total = sum(Weight)
half = total // 2
# possibleかimpossibleを返すだけなので、重さを気にする必要ない
# 全てのおもりを使って天秤が水平 => 片方に全重さ/2となるか判定

# おもり(100以下の重さのおもりが100個以下)

'''

重りの重さの合計が奇数のときimpossible


'''

# weight_sum = sum(W)
# weight_sum_half = weight_sum / 2

def check():
    if sum(Weight) % 2 != 0:
        print("impossible")
    else:
        half = sum(Weight) // 2
        '''
        # ex) 1 2 3
        # 重りの合計/2 = 3
        # 縦(重りの数) x 横(重りの合計/2)
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
         
        #dp[重りの数][重りの合計/2] : i番目まで見た時に重さjを作ることができるか判定していく

        '''
        dp = [[0 for i in range(half + 1)] for j in range(N + 1)]
        dp[0][0] = 1 # おもりを使わないとき
        for i in range(N):
            for j in range(half + 1):
                # 重りの重さ <= 半分の重さ
                if Weight[i] <= j:
                    dp[i + 1][j] = dp[i][j - Weight[i]] or dp[i][j]
                else:
                    dp[i + 1][j] = dp[i][j] 
            # 
    print(sum(Weight), sum(Weight) // 2)


if __name__ == "__main__":
    check()