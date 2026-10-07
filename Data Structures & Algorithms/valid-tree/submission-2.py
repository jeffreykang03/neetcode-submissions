class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        mark = set()
        def dfs(node, prev):
            if node in mark:
                return False
            mark.add(node)
            if len(adj[node]) == 1 and node != 0:
                return True
            for v in adj[node]:
                if v != prev:
                    print(v, node)
                    if not dfs(v, node):
                        return False
            return True
        ans = dfs(0, -1)
        if len(mark) == n:
            return ans
        return False