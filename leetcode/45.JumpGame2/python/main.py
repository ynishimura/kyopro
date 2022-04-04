

from typing import List


class Solution:
    def jump(self, nums):
        # 最小にしたい
        jumps = 0
        
        # 最も遠い
        farthest = 0
        
        # 位置
        current = right = 0

        # 範囲を選択
        # https://qiita.com/drken/items/ecd1a472d3a0e7db8dce
        # 尺取法に近い
        while right < len(nums) - 1:
            for i in range(current, right + 1):
                farthest = max(farthest, i + nums[i])
            current = right + 1
            right = farthest
            jumps += 1
            
        return jumps


s = Solution()
result = s.jump([2,3,1,1,4])
result = s.jump([1,2,3,4,5,6,7])
print(result)