from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 最小にしたい
        jumps = 0
        
        # 最も遠い
        farthest = 0
        
        # 位置
        current = right = 0

        while right < len(nums) - 1:
            for i in range(current, right + 1):
                farthest = max(farthest, i + nums[i])
            current = right + 1
            right = farthest
            jumps += 1
            
        return jumps