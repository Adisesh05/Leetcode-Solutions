class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        mat = [[-1] * m for _ in range(n)]
        que = []
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    mat[i][j] = 0
                    que.append((i, j))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r, c in que:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    que.append((nr, nc))
        return mat