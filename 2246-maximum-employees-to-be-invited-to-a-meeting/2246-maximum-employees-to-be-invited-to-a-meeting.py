class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        graph = defaultdict(list)
        transpose = defaultdict(list)
        for u, v in enumerate(favorite):
            graph[u].append(v)
            transpose[v].append(u)
        stack = []
        def fill(node):
            visited.add(node)
            for adjacent in graph[node]:
                if adjacent not in visited:
                    fill(adjacent)
            stack.append(node)
        sccs = []
        scc = set()
        def dfs(node):
            visited.add(node)
            scc.add(node)
            for adjacent in transpose[node]:
                if adjacent not in visited:
                    dfs(adjacent)
        visited = set()
        for u in graph:
            if u not in visited:
                fill(u)
        visited = set()
        while stack:
            u = stack.pop()
            if u not in visited:
                scc = set()
                dfs(u)
                sccs.append(scc)
        def arm(u, v):
            length = 0
            for adjacent in transpose[u]:
                if adjacent != v:
                    length = max(length, arm(adjacent, v)+1)
            return length
        clique = max((len(scc) for scc in sccs if len(scc) != 2), default=0)
        crowd = 0
        for u, v in [scc for scc in sccs if len(scc) == 2]:
            crowd += 2 + arm(u, v) + arm(v, u)
        return max(clique, crowd)