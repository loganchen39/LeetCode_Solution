# Algo. 1
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        : TC: 85.16%, O(n*m) for "for-loop" and "while-loop",
        : SC: 5.55%, O(1) for dict_order, 
        :
        :\Algo. 1 from Ligang, 1st idea, to use dict to store "order", so it will be easy and efficient  
        : to look up and compare. For 2 adjacent words, find their 1st different characters and compare 
        : with dict "order".
        """
        i = 0
        dict_order = {}
        for c in order:
            dict_order[c] = i
            i += 1
        
        n = len(words)
        if n <= 1: return True
        
        b_res = True
        for i in range(n-1):
            j      = 0
            l0, l1 = len(words[i]), len(words[i+1])
            min_l  = min(l0, l1)
            while j < min_l:
                if words[i][j] != words[i+1][j]:
                    if dict_order[words[i][j]] > dict_order[words[i+1][j]]: return False
                    else: break
                else:
                    j += 1
            #else:
            
            # Need to have "j == min_l"
            if j == min_l and l1 < l0: 
                return False
        
        return True

    


