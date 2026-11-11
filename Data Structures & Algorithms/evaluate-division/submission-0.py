class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        adj = defaultdict(list)
        for i in range(len(equations)):
            e, v = equations[i], values[i]
            adj[e[0]].append((e[1], v))
            adj[e[1]].append((e[0], 1 / v))

        def dfs(src, target, visited):
            if src not in adj or target not in adj:
                return -1
            if src == target:
                return 1

            visited.add(src)

            for nei, weight in adj[src]:
                if nei not in visited:
                    result = dfs(nei, target, visited)
                    if result != -1:
                        return weight * result

            return -1


        ans = []
        for q in queries:
            ans.append(dfs(q[0], q[1], set()))
        # print(ans)
        return ans