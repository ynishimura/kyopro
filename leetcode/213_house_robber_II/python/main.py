from typing import List

"""
range(4,7)
--> 4 5 6

range(0, 5, 1)
--> 0 1 2 3 4

range(0, 10, 2)
--> 0 2 4 6 8

range(10, 0, -1)
--> 10 9 8 7 6 5 4 3 2 1

range(0, -8, -2)
--> 0 -2 -4 -6

lo:ラストオーダー (Last Order)
動的計画法

はじめを取るときの配列、はじめを取らないときの配列を作って、
それぞれDPで計算して、大きい方が選ぶ
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return sum(nums)
        
        first_skip = self.sub_rob(nums, 0, len(nums)-2)
        first_get = self.sub_rob(nums, 1, len(nums)-1) 
        result = max(
            first_skip,
            first_get
        )

        return result

    def sub_rob(self, nums, start, hi):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        prev_prev = 0
        prev = 0
        for idx in range(start, hi+1):
            result = max(prev_prev+nums[idx], prev)
            prev_prev = prev
            prev = result
        return result


a = Solution()
print(a.rob([2, 3, 2]))
print(a.rob([1, 2, 3, 1]))
print(a.rob([1,1,3,6,7,10,7,1,8,5,9,1,4,4,3])) # 41()
