from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # find the number of connected components in a graph
        # im thinking the way to do this would be using cycles and seeing if we return to the same node => cycle
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        # build a hashmap
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        ans = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        
        return ans