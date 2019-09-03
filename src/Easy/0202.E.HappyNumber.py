# Algo. 1
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        : Input n (int):
        : Output (bool):
        :
        : TC: 5.96%, O(1) (O(100) = O(1)); 
        : SC: 5.26%, O(1); 
        :\Algo. 1 BF from Ligang, extract each digit and compute in a loop. 
        : Question: When to return False since it'll become endless loop? Set a MAX_LOOP number; 
        """
        MAX_LOOP = 100
        i = 1
        while i <= MAX_LOOP:
            m = 0
            while n > 0:
                d = n%10
                m += d**2
                n = int((n - d)/10)
            if m == 1: 
                return True
            else:
                n = m
            
            i += 1
                
        return False




# Algo. 2
class Solution:
    def isHappy(self, n):
        """
        :Input n (int): 
        :Output (bool): 
        :
        : TC: 5.96%, O(1)
        : SC: 5.26%, O(1)
        :\Algo. 2 BF from Ligang, use "str_n = str(n)" to make it a lot simpler!
        """
        MAX_LOOP = 100
        i_sum_sqr = 0
        
        for i in range(MAX_LOOP):
            str_n = str(n)
            n_len = len(str_n)
            for j in range(n_len):
                i_sum_sqr += int(str_n[j])**2
            if i_sum_sqr == 1:
                return True
            else:
                n = i_sum_sqr
                i_sum_sqr = 0
        
        return False


