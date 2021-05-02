class Solution:
    def getMinDistance(self, nums, target: int, start: int) -> int:
        "targetのインデックスを見つける"
        print(nums, target, start)
        # print(nums.index(target))
        # print([i for i, x in enumerate(nums) if x == target ][-1])
        indexs = [i for i, x in enumerate(nums) if x == target]
        print(f'indexs: {indexs}')
        if (start in indexs):
            print(0)
        
        "binary_search"
        if len(indexs) == 0:
            return None
        if len(indexs) == 1:
            print(abs(indexs[0] - start))
            return
        if (start == 0):
            print(indexs[0])
        min_diff = float('inf')
        imin = 0
        imax = len(indexs) -1
        closest_num = None
        while imin <= imax:
            imid = imin + (imax - imin) // 2
            #　中心の左右の値と目標との差を計算する。
            if imid + 1 < len(indexs):
                min_diff_right = abs(indexs[imid+1] - start)
            if imid >= 0:
                min_diff_left = abs(indexs[imid-1] - start)
            # 最初の差と最も最小に近い値を更新する。
            if min_diff_left < min_diff:
                min_diff = min_diff_left
                closest_num = indexs[imid-1]
            if min_diff_right < min_diff:
                min_diff = min_diff_right
                closest_num = indexs[imid+1]
            # 2分探索する。
            if indexs[imid] < start:
                imin = imid + 1
            elif indexs[imid] > start:
                imax = imid -1
            else:
                return indexs[imid]
        print(f'close {closest_num}')
        print(f'ans: {abs(closest_num - start)}')

a = Solution()
"expected => 0"
a.getMinDistance([1,1,1,1,1,1,1,1,1,1],1,9)

"expected => 1"
a.getMinDistance([1,2,3,4,5], 5, 3)
a.getMinDistance([1,1,1,1,1,1,1,1,1,1],1,0)
a.getMinDistance([1],1,0)
"expected => 1"
a.getMinDistance([1,5,3,4,5], 5 ,2)

"expected => 5 "
a.getMinDistance([1,1,1,1,1,10000,10000,10000,10000,10000],10000,0)


# class Solution:
#     def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
#         indexs = [i for i, x in enumerate(nums) if x == target]
#         if (start in indexs):
#             return 0
#         "binary_search"
#         if len(indexs) == 0:
#             return None
#         if len(indexs) == 1:
#             return abs(indexs[0] - start)
#         if (start == 0):
#             return(indexs[0])
#         min_diff = float('inf')
#         imin = 0
#         imax = len(indexs) -1
#         closest_num = None
#         while imin <= imax:
#             imid = imin + (imax - imin) // 2
#             #　中心の左右の値と目標との差を計算する。
#             if imid + 1 < len(indexs):
#                 min_diff_right = abs(indexs[imid+1] - start)
#             if imid >= 0:
#                 min_diff_left = abs(indexs[imid-1] - start)
#             # 最初の差と最も最小に近い値を更新する。
#             if min_diff_left < min_diff:
#                 min_diff = min_diff_left
#                 closest_num = indexs[imid-1]
#             if min_diff_right < min_diff:
#                 min_diff = min_diff_right
#                 closest_num = indexs[imid+1]
#             # 2分探索する。
#             if indexs[imid] < start:
#                 imin = imid + 1
#             elif indexs[imid] > start:
#                 imax = imid -1
#             else:
#                 return indexs[imid]
#         return abs(closest_num - start)