class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        def get_connected_component(src):
            q = deque([src]) 
            component = set([src])
            visit[src] = True 

            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if nei in component:
                        continue
                    q.append(nei)
                    component.add(nei)
                    visit[nei] = True  
            
            return component

        def longest_path(src):
            q = deque([(src, 1)])  
            dist = {src: 1}        
            while q:
                node, length = q.popleft()
                for nei in graph[node]:
                    if nei in dist:
                        if dist[nei] == length:
                            return -1  
                        continue
                    q.append((nei, length + 1))
                    dist[nei] = length + 1
            return max(dist.values())

        visit = [False] * (n + 1)
        res = 0
        for i in range(1, n + 1):
            if visit[i]:
                continue
            visit[i] = True
            components = get_connected_component(i)
            max_cnt = 0
            for src in components:
                length = longest_path(src)

                if length == -1:
                    return -1
                max_cnt = max(max_cnt, length)
            res += max_cnt
        return res