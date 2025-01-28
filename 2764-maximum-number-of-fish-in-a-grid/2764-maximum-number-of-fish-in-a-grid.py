class Solution:
    def bfs(self, i: int, j: int, grid: list[list[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n, m = len(grid), len(grid[0])
        queue = [(i, j)]
        front = 0  
        fish = grid[i][j]
        grid[i][j] = 0  
        while front < len(queue):
            x, y = queue[front]
            front += 1
            for dx, dy in directions:
                a, b = x + dx, y + dy
                if 0 <= a < n and 0 <= b < m and grid[a][b] > 0:
                    queue.append((a, b))
                    fish += grid[a][b]
                    grid[a][b] = 0  
        return fish

    def findMaxFish(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        mxFish = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    mxFish = max(mxFish, self.bfs(i, j, grid))
        return mxFish