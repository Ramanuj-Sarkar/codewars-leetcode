# For every row in a binary tree
# return a list of the values in the row from left to right.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()

            # add a new level if necessary
            if level == len(levels):
                levels.append([])

            levels[level].append(node.val)

            # the left comes out first
            # then the right because it's a stack
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        
        return levels
        
