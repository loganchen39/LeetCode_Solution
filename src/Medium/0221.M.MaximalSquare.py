# Algo. 1
import numpy as np
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        : TC: 5.43%, O(m*n*m*n) in worst case, like 4 for-loop
        : SC: 9.09%, O(m*n) for np_mat
        :
        :\1st idea, for each current 1, check toward right and down, to find the largest square.
        :\Algo. 1 BF from Ligang as the above 1st idea. Need to use numpy array to get the 2D sub-array!
        : Need to be very careful about dealing with 2D array, particularly when subscripting.
        """
        m = len(matrix)
        if m==0: return 0
        n = len(matrix[0])
        
        np_mat = np.array(matrix)
        
        max_len = 0
        for i in range(m):
            for j in range(n):
                if np_mat[i][j] == '1':
                    if max_len == 0: max_len = 1
                    for k in range(max_len, min(m-1-i, n-1-j)+1):
                        # if all(x=='1' for x in matrix[i:i+k+1][j:j+k+1]) and k+1>max_len:  # not gonna work!
                        # be aware of the following "all" and subscripting usage!
                        if k+1>max_len and all(all(x=='1' for x in elems) for elems in np_mat[i:i+k+1, j:j+k+1]):
                            max_len = k+1
                        else:
                            break
                        
        return max_len**2