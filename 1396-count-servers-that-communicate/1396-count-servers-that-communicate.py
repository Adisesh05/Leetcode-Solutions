class Solution:
    def countServers(self, grid):
        r, c = len(grid), len(grid[0])
        row, col = [0] * r, [0] * c
        servers = []
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
                    servers.append((i, j))
        return sum(row[i] > 1 or col[j] > 1 for i, j in servers)