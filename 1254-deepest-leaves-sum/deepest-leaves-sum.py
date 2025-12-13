# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        queue = deque([root])
        while queue:
            number_of_nodes = len(queue)
            rowsum = 0
            for _ in range(number_of_nodes):
                node = queue.popleft()

                # do something
                rowsum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if len(queue) == 0:
                return rowsum
        return 0