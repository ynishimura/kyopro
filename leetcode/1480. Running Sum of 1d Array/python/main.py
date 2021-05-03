from typing import List, Dict
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        result = []
        for i in nums:
            sum += i
            result.append(sum)
        return result

a = Solution()
a.runningSum([1,2,3,4])