# Algo. 1
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        : type matrix: List[List[int]]
        : rtype: List[int]
        :
        : TC: 73.25%, O(m*n); 
        : SC: 8.7%, O(m*n) for lst_res; 
        :\Algo. 1 BF from Ligang, move (i, j), and set visited element as None; be aware 4 loops of row/column 
        : become one complete process, so there's 4 while loops under the big outer while loop, but the whole 
        : loop may end and return at the end of any small loop, need to check every time to see if the next element
        : becomes None. 
        """
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        lst_res = []
        #if m == 1: lst_res = matrix[0][:]; return lst_res
        ## if n == 1: lst_res = matrix[:][0]; return lst_res  # NOT working!
        #if n == 1:  # the following code works without this firstly special case processed.
        #    for i in range(m):
        #        lst_res.append(matrix[i][0])
        #    return lst_res    
        
        #\Originally wanted them to be used as valid max/min row or column
        # The problem with them is you need to maintain and update them accordingly 
        # and then use them in end conditions. It's a lot easier to just set the visited
        # element as "visited", or like here: matrix[i][j] = None, and then they become like a "wall"
        # where your loop of element doesn't enter. 
        # rt, rb, cl, cr = 0, m-1, 0, n-1
        # 4 loops construct a complete process, and then repeat; However it may end and return at 
        # the end of any loop; 
        # direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # i, j direction, not used
        i, j = 0, 0
        while True:
            # i-direction +1
            while j < n and matrix[i][j] != None: lst_res.append(matrix[i][j]); matrix[i][j] = None; j += 1
            j -= 1
            i += 1
            if i >= m or matrix[i][j] == None: return lst_res
            while i < m and matrix[i][j] != None: lst_res.append(matrix[i][j]); matrix[i][j] = None; i += 1
            i -= 1
            j -= 1
            if j < 0 or matrix[i][j] == None: return lst_res
            while j >= 0 and matrix[i][j] != None: lst_res.append(matrix[i][j]); matrix[i][j] = None; j -= 1
            j += 1
            i -= 1
            if i < 0 or matrix[i][j] == None: return lst_res
            while i >= 0 and matrix[i][j] != None: lst_res.append(matrix[i][j]); matrix[i][j] = None; i -= 1
            i += 1
            j += 1
            if j >= n or matrix[i][j] == None: return lst_res

