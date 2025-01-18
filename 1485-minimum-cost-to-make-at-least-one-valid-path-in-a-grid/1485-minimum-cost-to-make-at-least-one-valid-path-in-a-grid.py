class Solution:
    def minCost(self, grid):
        rows, cols = len(grid), len(grid[0])
        sides = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        q = [(0, 0, 0)]
        visited = set()
        while q:
            row, col, cost = q.pop(0)
            if (row, col) == (rows - 1, cols - 1):
                return cost
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for d, (dr, dc) in sides.items():
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if grid[row][col] == d:
                        q.insert(0, (nr, nc, cost))
                    else:
                        q.append((nr, nc, cost + 1))