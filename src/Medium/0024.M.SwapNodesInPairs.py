# Algo. 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        : TC: 44.43%, O(n) for loop, 
        : SC: 6.06%, O(1),
        : 
        :\1st idea, loop and process.
        :\Algo. 1 BF from Ligang, loop and process. 
        """
        if not head or not head.next: return head
        
        p         = head
        p_next    = p.next.next
        head      = p.next
        head.next = p
        p.next    = p_next
        p_prev    = p
        p         = p_next
        
        while p and p.next:
            p_next      = p.next.next
            p_prev.next = p.next
            p.next.next = p
            p.next      = p_next
            p_prev      = p
            p           = p_next
        
        return head




