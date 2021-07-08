#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0


        n = len(prices)
        if n < 2: 
            return 0

        # 購入するため利益は減る
        prev_buy = -prices[0]
        prve_sell = 0
        prev_through = 0

        for i in range(1, n):
            buy = max(max(prve_sell, prev_through) - prices[i], prev_buy) # 利益が減るほうが少ない方
            sell = max(prev_buy + prices[i], prev_sell) # 
            through = max(prve_sell, prev_buy, prev_through)

            prev_buy, prev_sell, prev_through = buy, sell, through 

        return max(sell, through)
# @lc code=end

