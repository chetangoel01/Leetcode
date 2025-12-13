# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node, arr):
            if not node:
                return
            
            left = dfs(node.left, arr)
            arr.append(node.val)
            right = dfs(node.right, arr)

            return arr
        
        sortedArr = dfs(root, [])
        print(sortedArr)
        for i in range(len(sortedArr)-1):
            if sortedArr[i] >= sortedArr[i+1]:
                return False
        return True