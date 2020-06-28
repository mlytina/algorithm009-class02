#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return
        result = grid
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    result[i][j] += result[i][j - 1]
                elif j == 0:
                    result[i][j] += result[i - 1][j]
                else:
                    result[i][j] += min(result[i - 1][j], result[i][j - 1])
        return result[-1][-1]

# @lc code=end

