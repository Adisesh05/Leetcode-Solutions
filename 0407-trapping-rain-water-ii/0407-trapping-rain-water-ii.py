class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0
        rows, cols = len(heightMap), len(heightMap[0])
        heap, dirs = [], (0, 1, 0, -1, 0)
        for r in range(rows):
            for c in (0, cols - 1):
                heap.append((heightMap[r][c], r, c))
                heightMap[r][c] = -1
        for c in range(cols):
            for r in (0, rows - 1):
                heap.append((heightMap[r][c], r, c))
                heightMap[r][c] = -1
        heapify(heap)
        water = maxH = 0
        while heap:
            h, r, c = heappop(heap)
            maxH = max(maxH, h)
            for d in range(4):
                nr, nc = r + dirs[d], c + dirs[d + 1]
                if 0 <= nr < rows and 0 <= nc < cols and heightMap[nr][nc] != -1:
                    nh = heightMap[nr][nc]
                    water += max(0, maxH - nh)
                    heightMap[nr][nc] = -1
                    heappush(heap, (nh, nr, nc))
        return water