class Solution:
    def gridGame(self, grid):
        n = len(grid[0])
        up, down = sum(grid[0]) - grid[0][0], 0
        res = up
        for i in range(1, n):
            up -= grid[0][i]
            down += grid[1][i - 1]
            res = min(res, max(up, down))
        return res