class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev = [[] for _ in range(n)]
        out = [0] * n
        for i, nbrs in enumerate(graph):
            out[i] = len(nbrs)
            for nbr in nbrs:
                rev[nbr].append(i)
        q = [i for i in range(n) if out[i] == 0]
        safe = [False] * n
        while q:
            node = q.pop()
            safe[node] = True
            for p in rev[node]:
                out[p] -= 1
                if out[p] == 0:
                    q.append(p)
        return [i for i in range(n) if safe[i]]