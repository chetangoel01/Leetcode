# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node, arr):
            if not node:
                return
            
            left = dfs(node.left, arr)
            arr.append(node.val)
            right = dfs(node.right, arr)

            return arr

        sortedArr = dfs(root, [])
        # print(sortedArr)
        ans = math.inf
        for i in range(1, len(sortedArr)):
            ans = min(ans, sortedArr[i] - sortedArr[i-1])
        return ans