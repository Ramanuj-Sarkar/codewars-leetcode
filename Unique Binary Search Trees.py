# Given the number n, you add the number of 
# unique binary search trees with n nodes.
# each of which is numbered from 1 to n.
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # memory of starts and ends
        memory = {}

        # call other recursive function
        return self.findAllTrees(1, n, memory)

    # lower and upper bounds are inclusive
    def findAllTrees(self, lower: int, upper: int, memory: dict[int, int]) -> list[Optional[ListNode]]:
        # there can't be any nodes here
        if lower > upper:
            return [None]

        # dynamic programming
        if (lower, upper) in memory:
            return memory[(lower, upper)]
        
        answer = []
        
        for i in range(lower, upper + 1):
            # the left and right children of node i
            left_children = self.findAllTrees(lower, i - 1, memory)
            right_children = self.findAllTrees(i + 1, upper, memory)

            # you need to make new nodes each time
            for left in left_children:
                for right in right_children:
                    answer.append(TreeNode(i, left, right))
            
        # adding to dynamic list
        memory[(lower, upper)] = answer
        
        return answer
