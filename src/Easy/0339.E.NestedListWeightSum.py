# Algo. 1
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def __init__(self):
        self.sum_res = 0
        
        
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        : TC: 56.28%, O(n) n being the total number of the integer elements!
        : SC: 20%, O(depth), stack for recursion using depth.
        : 
        :\1st idea, how to loop over the nested list? Need to use recursion for these NESTED list? DFS need recursion!
        :\Algo. 1 using DFS (i.e. recursion) by Ligang, same as A.1, to deal with this kind of NESTED list.
        """
        def dfs(nl: NestedInteger, curr_lvl) -> int:
            if nl.isInteger():  # base case, operate on the member (global) variable self.sum_res.
                self.sum_res += curr_lvl*nl.getInteger()
            else: 
                if not nl: return
                else:
                    lst_nl = nl.getList()  # need to get the list first, NestInteger itself is not iterable.
                    for elem in lst_nl:
                        dfs(elem, curr_lvl+1)
        
        
        # this loop is necessary, first level is 1. 
        for elem in nestedList:
            dfs(elem, 1)
        return self.sum_res




