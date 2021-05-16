"""
memo化しておくとうまくいきそう
>> > 1 ^ 3
2
>> > 2 ^ 6
4
>> > 1 ^ 3 ^ 6
4
>> > 1 ^ 3 ^ 6
4
>> > 1 ^ 3 ^ 6 ^ 7
3
>> > 4 ^ 7
3
"""

from typing import List


class Solution:
    def subsetXORSum(self, A: List[int]) -> int:
        # init = 0
        # total = 0
        # counter = 0
        # while counter < len(nums):
        #     list = []
        #     for i, num in enumerate(nums):
        #         if(i <= counter):
        #             list.append(num)
        #             print(list)
        #             xor = 0
        #             if(len(list) <= 1):
        #                 xor = 0 ^ num
        #             else:
        #                 xor = init ^ num
        #                 print(f'{init}^{num}={xor}')
        #             total += xor
        #             init = num

        #     counter += 1
        # print(f'===> {total}')
        def go(i=0, x=0):
            if i == len(A):
                return x
            include = go(i + 1, x ^ A[i])  # ✅ case 1: include
            exclude = go(i + 1, x)         # 🚫 case 2: exclude
            return include + exclude
        return go()


sol = Solution()
print(sol.subsetXORSum([1, 3]))
print(sol.subsetXORSum([5, 1, 6]))
print(sol.subsetXORSum([3, 4, 5, 6, 7, 8]))
