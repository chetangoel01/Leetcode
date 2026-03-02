class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: compute rightmost 1 for each row
        rightmost = []
        for row in grid:
            pos = -1
            for j in range(n):
                if row[j] == 1:
                    pos = j
            rightmost.append(pos)

        swaps = 0

        # Step 2: greedy placement
        for i in range(n):
            j = i
            
            # find row that can satisfy position i
            while j < n and rightmost[j] > i:
                j += 1

            if j == n:
                return -1

            # bubble row j up to i
            while j > i:
                rightmost[j], rightmost[j-1] = rightmost[j-1], rightmost[j]
                swaps += 1
                j -= 1

        return swaps