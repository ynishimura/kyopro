from math import inf
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        print(nums)
        # ans = -inf
        # window_max_length = len(nums)
        # for i in range(window_max_length):
        #     cur_sum = 0
        #     window_size = i
        #     for j in range(window_size, len(nums)):
        #         position = j
        #         value = nums[position] 
        #         cur_sum += value
        #         ans = max(ans, cur_sum)
        # return ans

        dp = [[0]*len(nums) for i in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
            dp[0][i] = max
nums = [-2,1,-3,4,-1,2,1,-5,4]
# 捨てることができる
a = Solution().maxSubArray(nums)