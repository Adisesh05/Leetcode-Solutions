class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        index = {}
        for i in range(m):
            for j in range(n):
                index[mat[i][j]] = (i, j)
        row = [0] * m
        col = [0] * n
        for i, val in enumerate(arr):
            r, c = index[val]
            row[r] += 1
            col[c] += 1
            if row[r] == n or col[c] == m:
                return i
        return -1