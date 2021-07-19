#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:

        # すべての負の数は回文ではない
        if x < 0:
            return False
        ranger = 1

        # 桁数を求める
        while x / ranger >= 10:
            ranger *= 10
        
        while x:
            # 左の桁を取得
            left = x // ranger

            # 最後の桁を取得
            right = x % 10
            if left != right:
                return False
            
            # 桁をずらす
            x = (x % ranger) // 10
            ranger /= 100
        return True


a = Solution()
print(a.isPalindrome(-101)) 
# @lc code=end

