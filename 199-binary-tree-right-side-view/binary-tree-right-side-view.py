# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # basically we need the last node of each layer
        if not root:
            return []
        queue = deque([(root, 0)])
        output = []
        while queue:
            nodes_in_current_level = len(queue)
            d = 0
            for i in range(nodes_in_current_level):
                node, side = queue.popleft()

                # do operation
                # keep depth as the second parameter not the side. last one of the current depth to be ejected is part of the output
                if i == nodes_in_current_level - 1:
                    output.append(node.val)

                if node.left:
                    queue.append((node.left, d + 1))
                if node.right:
                    queue.append((node.right, d + 1))

        return output
