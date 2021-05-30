"""
https://leetcode.com/contest/weekly-contest-243/problems/check-if-word-equals-summation-of-two-words/
"""

import typing

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstWord_num = int(self.alpha2num(firstWord))
        secondWord_num = int(self.alpha2num(secondWord))
        targetWord_num = int(self.alpha2num(targetWord))

        if (firstWord_num + secondWord_num == targetWord_num):
            return True
        else:
            return False

    
    def alpha2num(self, word: str):
        
        list = []
        for i in word:
            list.append(str(ord(i) - ord('a')))
        string_num =  ''.join(list)
        return string_num
a = Solution()
print(a.isSumEqual('acb','cba','cdb'))
print(a.isSumEqual('aaa','a','aab'))
print(a.isSumEqual('aaa','a','aaaa'))
        