# Algo. 1
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):
    """
    : TC: 49.72%, O(n) for __init__, O(m) for hasNext and next,
    : SC: 58.06%, O(n) for self.stack
    : 
    :\1st idea, use recursion (the only way?) to deal with these nestedList problem?
    :\Algo. 1 from discuss "Simply Simple python solution - using stack", which is relatively easy to understand,
    : recursion is not the only way to deal with nestedList, you can also use while-loop (to unnest the list), plus 
    : stack for these certain problems. Theoratically recursion and loop are exchangable. Use stack to re-organize   
    : the data. Be aware that it only has two functions of "next" and "hasNext", so you do NOT over-think of other   
    : functions like "prev" or "curr".
    """

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        for i in range(len(nestedList)-1, -1, -1):
            self.stack.append(nestedList[i])
        

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext(): return None
        
        # [-1] means the last element
        if self.stack[-1].isInteger():
            # even you know it's an integer element, you still need the interface "getInteger()"
            # to get the value. 
            return self.stack.pop().getInteger()
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.stack: return False
        while not self.stack[-1].isInteger():
            lst_ni = self.stack.pop().getList()
            for i in range(len(lst_ni)-1, -1, -1):
                self.stack.append(lst_ni[i])
            if not self.stack: return False
        
        return True
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())




