"""
https://leetcode.com/contest/weekly-contest-243/problems/maximum-value-after-insertion/
"""

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        
        join_num = n + str(x)
        if('-' in join_num):
            max_num = sorted(join_num)
            return ''.join(max_num)
        else:            
            max_num = sorted(join_num, reverse=True)
            return ''.join(max_num)




a = Solution()
print(a.maxValue('99',9))
print(a.maxValue('99',1))
print(a.maxValue('-99',1))
print(a.maxValue('-132',3)) # ok"-1323"  ng:"-1233"