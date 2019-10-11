# Algo. 1
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        : TC: 56.67%, O(n*m)
        : SC: 15.38%, O(n*m) for D; 
        :
        :\1st idea, assume n1<=n2, at least it needs to insert (n2-n1) characters. If n1>=n2, reverse
        : operation. No idea.
        :\As indicated, using DP, which usually not recursion, normally use sth like a matrix/array to gradually
        : compute each element, to get the final results. Problem conversion/re-statement.
        :\Algo. 1 as A.1 DP, get the key relationship/formula, partially implemented by Ligang.
        """
        n, m = len(word1), len(word2)
        if n*m == 0: return n+m
        
        D = [[0]*(m+1) for _ in range(n+1)]  # D[n+1][m+1]
        for i in range(n+1): D[i][0] = i
        for j in range(m+1): D[0][j] = j
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                # This relationship is the KEY! Need to understand!
                D[i][j] = 1 + min(D[i-1][j], D[i][j-1], D[i-1][j-1] - 1*(word1[i-1]==word2[j-1]))
        
        return D[n][m]




