# Algo. 1
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        : TC: 28.59%, O(n) for for-loop
        : SC: 5.97%, O(n) for arr, 
        :
        :\1st idea, DP.
        :\Algo. 1 DP from Ligang, try to find the relationship between n and previous steps like n-1 and n-2,
        : It's like fibonachi array, using recursion will have a lot of redundent computation, TC will not be
        : good. So use an array (or just 2 vars) as bottom-up-DP. 
        """
        #def recur_func(n):
        #    if n == 1: return 1
        #    if n == 2: return 2
        #    return recur_func(n-1) + recur_func(n-2)
        
        if n == 1: return 1
        if n == 2: return 2
        
        arr = [0]*(n+1)
        arr[1] = 1
        arr[2] = 2
        for i in range(3, n+1):
            arr[i] = arr[i-1] + arr[i-2]
        
        return arr[n]




# Still Algo. 1
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        : TC: 67.89%, O(n) for for-loop
        : SC: 5.97%, O(1), same as O(n), should be wrong!? 
        :
        :\1st idea, DP.
        :\Still Algo. 1 DP from Ligang, using only 3 vars of a, b, c. 
        """
        if n == 1: return 1
        if n == 2: return 2

        a = 1
        b = 2
        for i in range(3, n+1):
            c = a+b
            a = b
            b = c
        
        return c


