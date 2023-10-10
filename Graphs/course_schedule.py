class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # adding set for visited course
        visiting = set()

        # if it is visited then we know its a circle then return false
        # if preMap[crs] is null, we know it can be reach return true
        # after then add course to visited
        # for every preMap do a dfs
        # then remove crs from visiting
        # and if all goes well set null list to current course and return true
        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        # check tieration for each course
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
