# to know the adjacent edges we built a empty list for each iteration
# create a set to know the visited position
# we are trying to know if current and previous value is equal or not
# we are using dfs for this method
# at first we need to check if the position is visited or not
# then add it to the list then for each adjacent run dfs
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        if not n:
            return True
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)
