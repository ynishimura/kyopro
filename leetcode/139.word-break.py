#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from typing import List

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                word = s[i: j+1]
                point = dp[i]
                if point and word in wordDict:
                    # どうやって更新しているのか
                    dp[j+1] = True
                    
        return dp[-1]

"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1] * len(s)
        def isSegmented(i):
            if i == len(s):
                return True
            if i > len(s):
                return False
            if dp[i] != -1:
                return dp[i]
            hasTrue = False
            for word in wordDict:
                if s[i:].startswith(word):
                    hasTrue |= isSegmented(i + len(word))
            dp[i] = hasTrue
            return hasTrue
        answer = isSegmented(0)
        return answer
"""
a = Solution()
# print(a.wordBreak("leetcode", ['leet', 'code']))
print(a.wordBreak("catsandog", ['cats','dog','sand','and','cat']))
# @lc code=end

