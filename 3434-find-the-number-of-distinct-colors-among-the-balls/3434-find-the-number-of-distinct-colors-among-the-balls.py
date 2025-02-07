class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        balls = {}
        colors = defaultdict(int)

        for x, y in queries:
            if x not in balls:
                balls[x] = y
            else:
                colors[balls[x]] -= 1
                if colors[balls[x]] == 0:
                    colors.pop(balls[x])
                balls[x] = y
            colors[y] += 1
            res.append(len(colors))
        return res