# Algo. 1
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        : type J: str
        : type S: str
        : rtype: int
        :
        : TC: O(ns*nj), 77.93%, 1 for-loop and 1 check if S[i] in J, 
        : SC: O(1), 5.47% (NOT correct!)
        :\Algo. 1 BF similar to A1, for-loop to check if it's a jewel.
        """
        nj, ns = len(J), len(S)
        if nj == 0 or ns == 0: return 0
        
        n_res = 0
        for i in range(ns):
            if S[i] in J: n_res += 1
        
        return n_res




# Algo. 2
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        : type J: str
        : type S: str
        : rtype: int
        :
        : TC: O(max(nj, ns)), 93.75%,  
        : SC: O(nj), 5.47% (NOT correct!), for set.
        :\Algo. 2 using set as HashTable, similar to A2, so the check of if it's jewel costs O(1) time!
        """
        nj, ns = len(J), len(S)
        if nj == 0 or ns == 0: return 0
        
        n_res = 0
        
        sj = set(J)
        # for i in range(nj): sj.add(J[i])
            
        for i in range(ns):
            if S[i] in sj: n_res += 1
        
        return n_res


