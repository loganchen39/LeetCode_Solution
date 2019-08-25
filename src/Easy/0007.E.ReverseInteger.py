# Algo. 1
class Solution:
    def reverse(self, x: int) -> int:
        """
        : type x: int
        : rtype: int
        :
        : TC: O(N), 84.14%, , N is the number of digits of x, which is about O(logx)!
        : SC: O(1), 5.23% (NOT correct!)
        :\Algo. 1 BF from Ligang, while-loop over each digit and accumulate, similar to Approach 1
        : "Pop and Push Digits & Check before Overflow"; My previous implementation is too complicated.
        """
        if abs(x) <= 9: return x
        
        n_res = 0
        # be aware that, -2%10 = 8, not 2! so we need to use abs. 
        abs_x = abs(x)
        
        while abs_x != 0:
            digit = abs_x%10
            n_res = n_res*10 + digit
            abs_x = int((abs_x - digit)/10)  # you can just use: abs_x = int(abs_x/10)
        
        if x < 0: n_res = -n_res
        if n_res > 2**31-1 or n_res < -2**31: n_res = 0
        return n_res

