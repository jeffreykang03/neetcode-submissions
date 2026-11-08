class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        ind = [0] * numCourses
        for p in prerequisites:
            adj[p[1]].append(p[0])
            ind[p[0]] += 1
        visit = set()
        from collections import deque
        q = deque()
        for i, n in enumerate(ind):
            if n == 0:
                q.append(i)
        ans = []
        while q:
            cur = q.popleft()
            if cur in visit:
                continue
            for nxt in adj[cur]:
                ind[nxt] -= 1
                if ind[nxt] == 0:
                    q.append(nxt)
            visit.add(cur)
            ans.append(cur)
        if len(ans) == numCourses:
            return ans
        else:
            return []
            