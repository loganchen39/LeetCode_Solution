# Algo. 1
class MinStack:
    """
    :\Algo. 1 BF from Ligang, it did NOT satisfy the condition of "retrieve the minimum element in CONSTANT time", 
    : it has Time Limit Exceeded error with 17/18 test cases passed.
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        n_len = len(self.stack)
        return self.stack[n_len-1]

    def getMin(self):
        """
        :rtype: int
        """
        res_min = self.stack[0]
        n_len = len(self.stack)
        for i in range(1, n_len):
            if self.stack[i] < res_min:
                res_min = self.stack[i]
        
        return res_min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




# Algo. 2
class MinStack:
    """
    : TC: 75.71%, all rest is O(1) except pop(), which in the worst case is O(n), on average it should be O(1)?
    : SC: 5.36%, 
    :\Algo. 2 from Ligang, just store an extra idx_min which points to the minimum.
    """

    def __init__(self):
        """
        :initialize your data structure here.
        """
        self.L = []
        self.idx_min = None
        

    def push(self, x: int) -> None:
        self.L.append(x)
        n = len(self.L)
        if n == 1: self.idx_min = 0
        elif x < self.L[self.idx_min]: self.idx_min = n-1
            

    def pop(self) -> None:
        if not self.L: return
        
        n = len(self.L)
        if n == 1: 
            self.L.pop()
            self.idx_min = None
            return
            
        if self.idx_min == n-1:
            self.idx_min = 0
            for i in range(1, n-1):
                if self.L[i] < self.L[self.idx_min]:
                    self.idx_min = i            
        self.L.pop()
            
        
    def top(self) -> int:
        if self.L: return self.L[len(self.L)-1]
        else: return None

        
    def getMin(self) -> int:
        if self.L: return self.L[self.idx_min]
        else: return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


