# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        : type lists: List[ListNode]
        : rtype: ListNode
        :
        : TC: O(M*logn), 37.66%, M is the total number of elements of all lists, n is the number of lists, 
        :     except for creating the heap in the first place, for the rest elements in
        :     the sorted lists, it takes logn TC. 
        : SC: O(1), 31.99%, should be O(M) for the result list? Did you allocate new space for the elements 
        :     in the result?
        :\Algo. 1 with heap sort, similar to Approach 3; 
        """
        def heapAdjust(lists: List[ListNode], s: int, e: int) -> None:
            """
            :\adjust only one node at s, down to e, it's assumed that all the tree structure below node s
            : are all heap structure. Be ware that when adjusting s, the "switch" (or the adjust) may go down 
            : several levels (times) until to the end (leaf), use a loop to implement this.
            :\We use an array (list) as the heap (complete tree) DS, then if the starting index is 1, then for 
            : node at idx, its left child is at 2*idx, and its right child is at 2*idx+1, and the last non-leaf
            : node is at int(n/2); if the starting index
            : is 0, then for node idx, its left and right child are at 2*idx+1 and 2*idx+2 respectively, ,and 
            : the last non-leaf node is at int((n-2)/2); So better to use the former rep!
            :\TC: O(logn) as the tree depth, 
            :\SC: O(1)
            """
            
            chd = 2*s
            while chd <= e:
                if chd+1 <= e:  # actually use a pointer j to point to the smaller child, then only one case to handle.
                    if lists[s].val <= lists[chd].val and lists[s].val <= lists[chd+1].val: break  # already a heap
                    else:
                        if lists[chd].val <= lists[chd+1].val:  # [s] switch with [chd]
                            # "UnboundLocalError: local variable 'tmp' referenced before assignment"
                            #tmp, lists[s], lists[chd] = lists[s], lists[chd], tmp
                            tmp        = lists[s]
                            lists[s]   = lists[chd]
                            lists[chd] = tmp
                            # WRONG! the result is different from seperating them into 2 lines as following!
                            # This is too tricky and dangerous!
                            #s, chd = chd, 2*s
                            s = chd
                            chd = 2*s
                        else:  # [s] swith with [chd+1]
                            # "UnboundLocalError: local variable 'tmp' referenced before assignment"
                            # tmp, lists[s], lists[chd+1] = lists[s], lists[chd+1], tmp
                            tmp          = lists[s]
                            lists[s]     = lists[chd+1]
                            lists[chd+1] = tmp
                            # WRONG! the result is different from seperating them into 2 lines as following!
                            # s, chd = chd+1, 2*s
                            s = chd+1
                            chd = 2*s
                else:  # chd+1 > e
                    if lists[s].val <= lists[chd].val: break  # already a heap
                    else: 
                        # "UnboundLocalError: local variable 'tmp' referenced before assignment"
                        # tmp, lists[s], lists[chd] = lists[s], lists[chd], tmp
                        tmp        = lists[s]
                        lists[s]   = lists[chd]
                        lists[chd] = tmp
                        break
        
        
        def heapSort(lists: List[ListNode]) -> None:
            """
            :\the idea is to adjust node from (tree) bottom-to-top, then when adjusting node idx, 
            : all the tree structure below idx are all valid heap structure.
            """
            # lists[1...n] for convenience of heap rep
            n = len(lists) - 1       
            for i in range(int(n/2), 0, -1):
                heapAdjust(lists, i, n)
                 
                    
                    
        #\Normally it's a bad idea to modify (e.g. delete or append) the list you're iterating over! 
        #for i in range(n):
        #    if not lists[i]: lists.pop(i)
        #print(lists)
        #filter(None, lists)  # not working
        
        # to remove all None [] element, special (corner) cases to handle first, or you need to 
        # handle later which is normally more complicated
        lists = [x for x in lists if x ]  
        if not lists: return None
        n = len(lists)
        if n == 1: return lists[0]
        
        # the valid node is [1...n], for convenience of left/right child ref. 
        LN_tmp = [ListNode(0)]
        lists = LN_tmp + lists  
        heapSort(lists)
        #lst_tmp = []
        #for i in range(1, len(lists)): lst_tmp.append(lists[i].val)
        #print(lst_tmp)
        
        # p_res and p_curr are new space-allocated elements? not just a reference (or pointer)?
        p_res = p_curr = lists[1]
        while p_curr:
            # lists[1] is already the minimum
            if lists[1].next:  # only these 2 cases
                lists[1] = lists[1].next
                heapAdjust(lists, 1, len(lists)-1)
                #lst_tmp = []
                #for i in range(1, len(lists)): lst_tmp.append(lists[i].val)
                #print(lst_tmp)
                
                p_curr.next = lists[1]
                p_curr = p_curr.next
            else:
                # lists.pop(1)  # better not pop here.
                # need to ask what is the "end condition"!
                if len(lists) <= 2: break  
                    
                # substitute the 1st element with the last element, and then adjust
                lists[1] = lists[len(lists)-1]  
                lists.pop(len(lists)-1)  # pop the last element
                    
                heapAdjust(lists, 1, len(lists)-1)
                
                #lst_tmp = []
                #for i in range(1, len(lists)): lst_tmp.append(lists[i].val)
                #print(lst_tmp)
                
                p_curr.next = lists[1]
                p_curr = p_curr.next
        
        return p_res


# Algo.1 with minor code improvement 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        : type lists: List[ListNode]
        : rtype: ListNode
        :
        : TC: O(M*logn), 38.74%, M is the total number of elements of all lists, n is the number of lists, 
        :     except for creating the heap in the first place, for the rest elements in
        :     the sorted lists, it takes logn TC. 
        : SC: O(1), 31.19%, should be O(M) for the result list? Did you allocate new space for the elements 
        :     in the result?
        :\Algo. 1 with heap sort, similar to Approach 3; 
        """
        def heapAdjust(lists: List[ListNode], s: int, e: int) -> None:
            """
            :\adjust only one node at s, down to e, it's assumed that all the tree structure below node s
            : are all heap structure. Be ware that when adjusting s, the "switch" (or the adjust) may go down 
            : several levels (times) until to the end (leaf), use a loop to implement this.
            :\We use an array (list) as the heap (complete tree) DS, then if the starting index is 1, then for 
            : node at idx, its left child is at 2*idx, and its right child is at 2*idx+1, and the last non-leaf
            : node is at int(n/2); if the starting index
            : is 0, then for node idx, its left and right child are at 2*idx+1 and 2*idx+2 respectively, ,and 
            : the last non-leaf node is at int((n-2)/2); So better to use the former rep!
            :\TC: O(logn) as the tree depth, 
            :\SC: O(1)
            """
            
            rc = lists[s]
            
            # for this kind of loop where you need to set the loop var j = 2*j, better to use while-loop!
            # here you'll have error of "UnboundLocalError: local variable 'j' referenced before assignment"
            # or name 'j' is not defined.
            # for j in range(2*s, e+1, 2*j):  # "UnboundLocalError: local variable 'j' referenced before assignment"
            #for j in range(2*s, e+1):
            #    if j+1 <= e and lists[j].val > lists[j+1].val: j += 1
            #    if lists[s].val <= lists[j].val: break
            #    else:
            #        lists[s] = lists[j]
            #        s        = j
            #        j        = 2*j  # also not working, j is still loop over: 2*s, 2*s+1, 2*s+2, ..., e!
            #lists[s] = rc
            
            j = 2*s
            while j <= e:
                if j+1 <= e and lists[j].val > lists[j+1].val: j += 1
                # ATTENSION: here it IS rc.val, if you want to compare with or use lists[i].val, then you need to
                # switch lists[s] with lists[j]! 
                if rc.val <= lists[j].val: break
                else:
                    # one-way assignment, not switching, 
                    lists[s] = lists[j]
                    s        = j
                    j        = 2*j
            lists[s] = rc  # assign the last non-conforming heap node with the starting rc node.
                
        
        def heapSort(lists: List[ListNode]) -> None:
            """
            :\the idea is to adjust node from (tree) bottom-to-top, then when adjusting node idx, 
            : all the tree structure below idx are all valid heap structure.
            """
            n = len(lists) - 1       
            for i in range(int(n/2), 0, -1):
                heapAdjust(lists, i, n)
                                     
        
        lists = [x for x in lists if x ]  
        if not lists: return None
        n = len(lists)
        if n == 1: return lists[0]
        
        LN_tmp = [ListNode(0)]
        lists  = LN_tmp + lists  
        heapSort(lists)
        
        # are p_res and p_curr just the ref (i.e. pointer) or new allocated object? if latter, 
        # p_res and p_curr are independent, and p_res is not linked to the rest node elements, 
        # then it should be wrong? But it passed all the test!
        p_res = p_curr = lists[1]
        while p_curr:
            # setup lists[1] for adjusting
            if not p_curr.next:
                if len(lists) <= 2: break  # end condition             
                lists[1] = lists[len(lists)-1] 
                lists.pop(len(lists)-1)
            else: 
                lists[1] = lists[1].next
                
            heapAdjust(lists, 1, len(lists)-1)  
            p_curr.next = lists[1]
            p_curr = p_curr.next
        
        return p_res

