# Algo. 1
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        : Input digits: str
        : Output: List[str]
        :
        : TC: 92.41%, worst case O(4^n), normally O(3^n),   
        : SC: 5.88%, worst case O(4^n+4^(n-1)+4^(n-2)+...+4^1), stack for recursive? lst_prev for each recursive step.
        :\Algo. 1 from Ligang using recursion. For this kinda of problem where the result is dependent on the previous/last 
        : step, recursion is a natural choice. Use HashTable (Dictionary) to store the digit2letter mapping info.
        : Any better algo.?
        """
        dict_dgt2ltr = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"]  
                     ,  "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        n = len(digits)
        if n == 0: return []
        if n == 1: return dict_dgt2ltr[digits[0]]
        
        
        def recursive_func(digits: str) -> List[str]: 
            n = len(digits)
            if n == 0: return []
            if n == 1: return dict_dgt2ltr[digits[0]]
            
            lst_prev = recursive_func(digits[0:n-1])
            lst_curr = []
            for i in range(len(lst_prev)):
                for j in range(len(dict_dgt2ltr[digits[n-1]])):
                    lst_curr.append(lst_prev[i] + dict_dgt2ltr[digits[n-1]][j])
                    
            return lst_curr
        
        
        return recursive_func(digits)




