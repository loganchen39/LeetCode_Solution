# Algo. 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        : type l1: ListNode
        : type l2: ListNode
        : rtype  : ListNode
        :
        : TC: 65.18%, O(m+n) worst case, O(min(m, n)) best case;
        : SC: 5.34%, O(1), why the actual percent is so low? The problem might lie in leetcode.com,
        : I ran exactly the same code that was finished 6 months ago, and the memory usage if from 6.5M
        : to 13.8M!; 
        :\Algo. Two-Pointers with a while-loop; 
        """
        
        # special cases to deal with first
        if not l1 and not l2: return None
        if not l1 and l2: return l2
        if l1 and not l2: return l1
        
        # initialize
        p1, p2 = l1, l2
        if p1.val <= p2.val: p = p1; p1 = p1.next; p_curr = p
        else: p = p2; p2 = p2.next; p_curr = p
            
        while p1 and p2:
            if p1.val <= p2.val: p_curr.next = p1; p_curr = p1; p1 = p1.next
            else: p_curr.next = p2; p_curr = p2; p2 = p2.next
        
        # different final cases
        if not p1 and p2:
            p_curr.next = p2
        elif p1 and not p2:
            p_curr.next = p1
        
        return p


# Copied from Approach 2 and accepted by leetcode, similar to the above algo.
# do NOT understand the code yet, will get back later. No initialize!
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        : type l1: ListNode
        : type l2: ListNode
        : rtype  : ListNode
        :
        : TC: 64.18%, O(m+n)
        : SC: 5.34%, O(1), why the actual percent is so low?
        :\Algo. Two-Pointers with a while-loop, copied from Approach 2;
        """
        
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next




# Algo. 2, as Approach 1 Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        : type l1: ListNode
        : type l2: ListNode
        : rtype  : ListNode
        :
        : TC: 90.00%, O(m+n);
        : SC: 5.34% (not correct), O(m+n) for the recursive stack; 
        :\Algo. recusion as Approach 1;
        """
        
        if not l1 and not l2: return None
        if not l1 and l2: return l2
        if l1 and not l2: return l1
        
        def merge(p1, p2):
            if not p1: return p2
            if not p2: return p1
            if p1.val <= p2.val: p1.next = merge(p1.next, p2); return p1
            else: p2.next = merge(p1, p2.next); return p2
        
        return merge(l1, l2)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        : type l1: ListNode
        : type l2: ListNode
        : rtype  : ListNode
        :
        : TC: 90.00%, O(m+n);
        : SC: 5.42% (not correct), O(m+n) for the recursive stack; 
        :\Algo. recusion, copied from Approach 1;
        """
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2