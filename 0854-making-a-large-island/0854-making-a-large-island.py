class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = island
                return dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1) + 1
            return 0

        m, n = len(grid), len(grid[0])
        island, areas = 2, {}
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                areas[island] = dfs(i, j)
                island += 1
                
        tarea = max(areas.values(), default = 0)
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 0:
                area, visland = 1, set()
                for ii, jj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] > 0 and grid[ii][jj] not in visland:
                        area += areas[grid[ii][jj]]
                        visland.add(grid[ii][jj])    
                tarea = max(area, tarea)
        return tarea