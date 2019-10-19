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
        # use member variables as global variables to keep record the result.
        self.max_lvl, self.sum_res = 0, 0
    
    
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        """
        : TC: 57.65%, O(n), n being the total number of integer elements.
        : SC: 25%, O(d), d being the maximum depth.
        : 
        :\1st idea, loop over each element, for each element, use while-loop and process accordingly.
        : First question, should we get the mamimum level first (which should be relatively easier to implement)? 
        : Or we can process gradually and use some formula to accumulate the sum? For the latter, if the 
        : element with deepest level comes first, like [[4, [6]], 1], we should keep the current max level?
        :\The above idea is not appropriate. So far I can think of only one method of RECURSION (DFS) to deal with 
        : the NESTED list! 
        :\Algo. 1 using recursion (DFS) for nested list from Ligang, based on the experience of problem 339. 
        """
        def dfs_getMaxLvl(ni: NestedInteger, curr_lvl):
            if ni.isInteger():  
                # base case, keep record of the maximum level.
                if curr_lvl > self.max_lvl: self.max_lvl = curr_lvl
            else:
                lst_ni = ni.getList()
                for elem in lst_ni:
                    dfs_getMaxLvl(elem, curr_lvl+1)
        
        
        def dfs_getSum(ni: NestedInteger, curr_lvl):
            # this recursion function is similar to problem 339.
            if ni.isInteger():
                # base case, accumulate, after you get the self.max_lvl.
                self.sum_res += ni.getInteger() * (self.max_lvl + 1 - curr_lvl)
            else:
                lst_ni = ni.getList()
                for elem in lst_ni:
                    dfs_getSum(elem, curr_lvl+1)
        
        
        # get the deepest level first
        for elem in nestedList:
            dfs_getMaxLvl(elem, 1)
        # print("max_lvl = " + str(self.max_lvl))
        
        # get the weighted sum
        for elem in nestedList:
            dfs_getSum(elem, 1)
        return self.sum_res




