class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], qry: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(n)]
        for u, v in pre:
            g[u].append(v)
        vis = [0] * n
        reachable = [set() for _ in range(n)]
        def dfs(node):
            if vis[node]:
                return reachable[node]
            vis[node] = 1
            for nbr in g[node]:
                reachable[node].add(nbr)
                reachable[node].update(dfs(nbr))
            return reachable[node]
        for u in range(n):
            dfs(u)
        return [v in reachable[u] for u, v in qry]