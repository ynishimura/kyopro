from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return sum(nums)
        return max(
            self.sub_rob(nums, 0, len(nums)-2),
            self.sub_rob(nums, 1, len(nums)-1)
        )

    def sub_rob(self, nums, lo, hi):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = prev_prev = prev = 0
        for idx in range(lo, hi+1):
            result = max(prev_prev+nums[idx], prev)
            prev_prev = prev
            prev = result
        return result


a = Solution()
print(a.rob([1, 2, 3, 1]))
