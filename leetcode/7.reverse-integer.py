#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # True - False => 1
        # False - False => 0
        # True - True => 0
        # False - True => -1
        s: int = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        # 32bit 2の32乗
        return s*r * (r < 2**31)
        
# @lc code=end

