# Algo. 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        : type head: ListNode
        : rtype: ListNode
        :
        : TC: O(n), 95.47%, if you run more times in the same webpage, the percentage may go down; 
        : SC: O(1), 28.16%
        :\Algo. 1 with while iteration as Approach 1, 3 pointers to reverse a linked list.
        """
        # corner cases
        if not head or not head.next: return head
        if not head.next.next:
            p0, p1 = head, head.next
            p0.next, p1.next = None, p0
            head = p1
            return head
        
        p0, p1, p2 = head, head.next, head.next.next
        p0.next = None
        while p2.next:
            p1.next = p0
            p0, p1, p2 = p1, p2, p2.next  # ok?
        
        # last 3 elements
        p1.next = p0
        p2.next = p1
        head    = p2
        
        return head


# Algo. 1
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        : type head: ListNode
        : rtype: ListNode
        :
        : TC: O(n), 56.26%
        : SC: O(1), 28.51%
        :\Algo. 1 with while iteration as Approach 1, with pointer curr and prev; a lot 
        : easier to understand and implement.
        """
        prev, curr = None, head
        while curr:
            pnext = curr.next
            curr.next = prev
            prev = curr
            curr = pnext
        return prev




# Algo. 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        : type head: ListNode
        : rtype: ListNode
        :
        : TC: O(n), 95.47%
        : SC: O(n) for recursion stack, 5.06%
        :\Algo. 2 with recursion, with pointer curr and prev, the idea is similar to algo. 1 with iteration.
        : it's different from Approach 2, need to check.
        """
        def helper(prev: ListNode, curr: ListNode) -> ListNode:
            if not curr: return prev
            pnext     = curr.next
            curr.next = prev
            return helper(curr, pnext)
            
        prev, curr = None, head
        return helper(prev, curr)

