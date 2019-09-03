# Algo. 1
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        : Do not return anything, modify s in-place instead.
        :
        : TC: 81.37%, O(n)
        : SC: 5.81%, O(1)
        :\Algo. 1 BF from Ligang, regular head-tail switch in a for-loop. 
        """
        n = len(s)
        if n <= 1: return
        
        for i in range(int(n/2)):
            ch = s[i]
            s[i] = s[n-1-i]
            s[n-1-i] = ch
            
        return

