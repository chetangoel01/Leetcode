# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        stack = []
        stack.append((root, targetSum))
        while stack:
            node, curr = stack.pop()
            if not node.left and not node.right and curr - node.val == 0:
                return True

            if node.left:
                stack.append((node.left, curr - node.val))
            if node.right:
                stack.append((node.right, curr - node.val))

        return False