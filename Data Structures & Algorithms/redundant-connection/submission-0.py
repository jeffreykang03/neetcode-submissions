class Solution:
    def findRedundantConnection(self, edges):

        adj = defaultdict(list)

        def dfs(node, target, visited):
            if node == target:
                return True

            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True

            return False

        for u, v in edges:
            if dfs(u, v, set()):
                return [u, v]

            adj[u].append(v)
            adj[v].append(u)