# Given a linked list, swap every two adjacent nodes.
# Return the head of the list. Don't change the values.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        first, second = head, head.next
        
        # it works by solving a smaller subproblem
        first.next = self.swapPairs(second.next)
        
        # This is how you update the pointer
        # of what is now the "previous" node
        second.next = first    
        
        return second
        
