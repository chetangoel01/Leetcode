class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # input is an adjacency list
        # do dfs, build the seen set
        # return true if length of seen = length of list


        def dfs(start):
            for node in rooms[start]:
                if node not in seen:
                    seen.add(node)
                    dfs(node)
        
        seen = {0}
        dfs(0)

        return len(seen) == len(rooms)