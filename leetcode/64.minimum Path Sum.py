"""
左うえから右下へ
"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        # 表を作成
        cost = [[0]*N for _ in range(M)]
        # 最初はgridそのまま設定
        cost[0][0] = grid[0][0]
        # 横のコストを計算
        for j in range(1,N):
            before_cost = cost[0][j-1]
            j_cost = grid[0][j] + before_cost
            cost[0][j] = j_cost
        # 縦のコストを計算
        for i in range(1,M):
            i_cost = grid[i][0] + cost[i-1][0]
            cost[i][0] = i_cost
        # 交差している、内部のところを計算
        for i in range(1,M):
            for j in range(1,N):
                # i,jの小さい方法を採用
                i_cost = cost[i-1][j]
                j_cost = cost[i][j-1]
                cross_cost = min(i_cost, j_cost) + grid[i][j]
                cost[i][j] = cross_cost
        return cost[M-1][N-1]
grid = [[1,3,1],[1,5,1],[4,2,1]] # => 7

Solution().minPathSum(grid)
