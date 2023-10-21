# classic dfs approach with hashmap for reference
# create a hasmap of tickets from src to sorted distance
# since we start of jfk airport we can append jfk to result list
# length of our result is total tickets + 1 since we are counting jfk
# when we iterate with the value of current source use a dfs approach on it to iterate over every edges
# pop the visited from the hashmap and add to result and after backtrack insert again to index and pop from result

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(Solution().findItinerary(tickets))
