class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        mark = set()
        def dfs(node):
            mark.add(node)
            for v in adj[node]:
                if v not in mark:
                    dfs(v)
            return
        ans = 0
        for i in range(n):
            if not i in mark:
                ans += 1
                dfs(i)
        return ans
