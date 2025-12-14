from collections import defaultdict
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(start):
            for node in graph[start]:
                if node not in seen:
                    seen.add(node)
                    dfs(node)

        graph = defaultdict(list)

        rows = len(grid)
        cols = len(grid[0])
        landcells = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    landcells.append((i, j))
                    # up
                    if i - 1 >= 0 and grid[i - 1][j] == "1":
                        graph[(i, j)].append((i - 1, j))
                    # down
                    if i + 1 < rows and grid[i + 1][j] == "1":
                        graph[(i, j)].append((i + 1, j))
                    # right
                    if j + 1 < cols and grid[i][j + 1] == "1":
                        graph[(i, j)].append((i, j + 1))
                    # left
                    if j - 1 >= 0 and grid[i][j - 1] == "1":
                        graph[(i, j)].append((i, j - 1))

        seen = set()
        ans = 0

        for cell in landcells:
            if cell not in seen:
                ans += 1
                seen.add(cell)
                dfs(cell)

        return ans
