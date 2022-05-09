# 面積をメモしていく
# たて、よこ、面積

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height)-1
        max_area = 0
        while left_index < right_index:
            # 容器から水が落ちるから、最小の高さを求める
            tate = min(height[left_index], height[right_index]) 
            yoko = right_index - left_index
            area = yoko * tate
            max_area = max(area,max_area)
            # 右の高さが大きいとき、左の高さをずらす
            if height[left_index] < height[right_index]:
                left_index = left_index+1
            else:
                right_index = right_index-1
        return max_area
