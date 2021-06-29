from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        # 後ろから見ていく、はじめ一番後ろを最大の数値に設定する
        max = prices[len(prices)-1]
        profit = 0

        for item in prices[::-1]:
            # 一番うしろから比較していく
            # 利点がでるとき
            if max - item > profit:
                profit = max - item
            # 最大の値を更新
            if item > max:
                max = item

        return profit


a = Solution()
a.maxProfit([7, 1, 5, 3, 6, 4])
