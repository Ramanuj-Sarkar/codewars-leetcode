# Reverse the nodes of a linked list k at a time
# If the number of nodes is not a multiple of k
# those nodes should remain as-is
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # start and end are inclusive
    def reverseThis(start: ListNode, end: ListNode) -> None:
        # set prev to the END
        # and curr to the START
        # so this is reversed later
        prev, curr = end, start

        while curr != end:
            # get the original next value
            temp = curr.next

            # set the new next value
            curr.next = prev

            # this is the new first value
            prev = curr

            # this is closer to the end now
            curr = temp
        
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            # empty
            return head
        
        # maybe the whole thing is unchanged
        nodes_remaining = 0
        length_finder = head
        while length_finder:
            length_finder = length_finder.next
            nodes_remaining += 1
        
        '''
        if total < k:
            # whole thing is unchanged
            return head
        '''
        
        # create a node that changes
        # which is originally in front of the head
        pre_head = ListNode()
        pre_head.next = head
        big_changes = pre_head

        while nodes_remaining >= k:
            small_changes = big_changes
            l = k
            while l > 0:
                small_changes = small_changes.next
                l -= 1
            end = small_changes.next
            start = big_changes.next
            
            # start reversing
            prev, curr = end, start

            while curr != end:
                # get the original next value
                temp = curr.next

                # set the new next value
                curr.next = prev

                # this is the new first value
                prev = curr

                # this is closer to the end now
                curr = temp
            
            # head of reversed group
            big_changes.next = prev
            
            # tail of reversed group
            big_changes = start
            
            # decrease remaining nodes
            nodes_remaining -= k
        
        return pre_head.next
