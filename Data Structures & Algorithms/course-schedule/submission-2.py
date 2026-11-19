class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        adj = defaultdict(list)
        ind = defaultdict(int)
        
        for u, v in prerequisites:
            adj[v].append(u)
            ind[u] += 1
            ind[v] += 0

        from collections import deque
        q = deque()

        for k in ind.keys():
            if ind[k] == 0:
                q.append(k)
        
        while q:
            cur = q.popleft()
            for neigh in adj[cur]:
                ind[neigh] -= 1
                if ind[neigh] == 0:
                    q.append(neigh)
        print(ind)
        for k in ind.keys():
            if ind[k] != 0:
                return False
        return True

        