#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = []
        len_strings = len(s)
        if not len_strings:
            return result

        if len_strings == 1:
            print(s)
            return s
        
        if len_strings == 2:
            print(s[0])
            return s[0]
        
        for i in range(1, len_strings-1):
            [result.append(s) for s in self.find_palindrome(s, i-1, i+1)]
            [result.append(s) for s in self.find_palindrome(s, i-1, i)]
        print(result)
        result.sort()
        print(result[-1])
        return result[-1]
    
    def find_palindrome(self, strings: str, left:int, right: int):
        result = []
        while 0 <= left and right <= len(strings) -1:
            if strings[left] != strings[right]:
                break
            result.append(strings[left: right+1])
            left -= -1
            right += 1
        return result
        
# @lc code=end

a = Solution()
a.longestPalindrome('babad') #=> bab
a.longestPalindrome('cbbd') # => bb
a.longestPalindrome('a') # => a
a.longestPalindrome('ac') # => a
a.longestPalindrome('ccc') # => ccc
a.longestPalindrome('abb') # => ccc