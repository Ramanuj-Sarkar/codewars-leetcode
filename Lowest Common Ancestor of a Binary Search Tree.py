# Find the lowest node in the binary search tree
# which has both p and q as descendants
# (a node can be a descendant of itself).
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        # the BST is sorted, so you know
        # the node has to be in this area
        while curr:
            if curr.val < p.val and curr.val < q.val:
                # the right child is greater
                # so we go there
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                # the left child is less
                # so we go there
                curr = curr.left
            else:
                # this has to be a node
                # and it's between them
                # so it's the answer
                return curr
        
        return curr
