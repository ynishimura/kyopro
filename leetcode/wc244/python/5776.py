from typing import List;
"""
https://qiita.com/rudorufu1981/items/5341d9603ecb1f9c2e5c
https://jackee777.hatenablog.com/entry/2019/05/03/223646
"""

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        # if mat == target:
        #     return True
        # right90 = list(map(list, (zip(*mat[::-1]))))
        # # print(f'right90mat:{right90}, target:{target}')
        # if right90 == target:
        #     return True
        # right180 = list(map(list, (zip(*right90[::-1]))))[::-1]
        # print(f'right180mat:{right180}, target:{target}')

        # if right180 == target:
        #     return True
                
        # right270 = list(map(list, (zip(*right180[::-1]))))[::-1]

        # if right270 == target:
        #     return True
        # left90 = mat[::-1]
        # if left90 == target:
        #     return True
        # return False
        for _ in range(4): 
            if mat == target: return True
            mat = [list(x) for x in zip(*mat[::-1])]
        return False 


a = Solution()
print(a.findRotation([[0,1],[1,0]], [[1,0],[0,1]]))
print(a.findRotation([[0,1],[1,1]], [[1,0],[0,1]]))

# true
print(a.findRotation([[0,0],[0,1]], [[0,0],[1,0]]))

# true
print(a.findRotation([[1,1],[0,1]], [[1,1],[1,0]]))

# true
print(a.findRotation([[1,0],[0,1]], [[1,0],[0,1]]))

# true
print(a.findRotation([[1,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,1]]))

print(a.findRotation([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]))

