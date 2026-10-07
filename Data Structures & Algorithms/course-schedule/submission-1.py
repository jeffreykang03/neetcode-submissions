class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mappa = {}
        for i in range(numCourses):
            mappa[i] = []
        for c, preq in prerequisites:
            mappa[c].append(preq)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if mappa[crs] == []:
                return True
            visiting.add(crs)
            for c in mappa[crs]:
                if not dfs(c):
                    return False
            visiting.remove(crs)
            mappa[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True