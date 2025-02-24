class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        bobPath = [bob]
        def getBobPath(bob, prev):
            if bob == 0:
                return True 
            
            for nei in graph[bob]:
                if nei == prev: continue
                bobPath.append(nei)
                if getBobPath(nei, bob): return True
                bobPath.pop()

            return False 

        getBobPath(bob, -1)
        if (len(bobPath)-1) % 2 == 0:
            for i in range((len(bobPath)-1)//2):
                amount[bobPath[i]] = 0
            amount[bobPath[(len(bobPath)-1)//2]] //= 2
        else:
            for i in range(len(bobPath)//2):
                amount[bobPath[i]] = 0

        res = float('-inf')
        def dfs(node, prev, money):
            nonlocal res
            if len(graph[node]) == 1 and graph[node][0] == prev:
                res = max(res, money + amount[node])
                return

            for nei in graph[node]:
                if nei == prev: continue
                dfs(nei, node, money + amount[node])

        dfs(0, -1, 0)
        return res