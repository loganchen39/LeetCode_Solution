# Algo. 1, 
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        : TC: 9.37%, worst case O(m^2*n^2);
        : SC: 6.25%, O(m) for lst;
        :
        :\First thought, this kind of maximal problem should be suitable for DP, will check out later.
        :\Algo. 1 BF from Ligang, My intial simple idea to compute the maximum for each (i, j) element, 
        : towards RIGHT and DOWN, by simple loop and checking, seems feasible, but when implementing, it's 
        : just NOT FEASIBLE. According to this idea, the maximum at (1, 0) is 3 (can only move towards right  
        : and down, and not counting the element at (0, 0)), the maximum at (0, 2) is 3, for (1, 2) it's 6, 
        : and for (1, 3) it's 4. 
        :\The above idea has been successfully implemented. For each nonzero-element at (i,j), 
        : compute row by row (towards down) the maximum number of continuous "1" (towards right), the max_col
        : in while-loop for bottom rows is bounded by top rows. For element (0, 2), it only has one 1, so for
        : rows 1 and 2, it only check up to one 1, to make it a valid rectangle. Use a list to store
        : each row's number of 1s, and then compare to get the maximal rectangle value. 
        :\The real dump BF scan all possible rectangle to see if it's valid (all 1s), to get the maximum. 
        : The TC would be too bad as O(m^3*n^3). 
        """
        if not matrix or not matrix[0]: return 0
        
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                
        for i in range(m):
            for j in range(n):
                # print("i = " + str(i) + ", j = " + str(j) + ", matrix[i][j] = " + str(matrix[i][j]))
                if matrix[i][j] == 0: 
                    continue
                    
                # max_ij  = 1
                lst     = []
                b_break = False
                max_col = n
                for k in range(i, m):
                    if b_break: break
                    #for l in range(j, n):
                    l = j
                    while l < max_col:
                        # print("k = " + str(k) + ", l = " + str(l) + ", matrix[k][l] = " + str(matrix[k][l]))
                        if matrix[k][l] == 0: 
                            if l == j: 
                                b_break = True
                            lst.append(l-j)
                            max_col = l  # not work for for-loop
                            break
                        else:
                            l += 1
                            if l >= max_col:
                                # max_col = n
                                lst.append(l-j)
                #print("i = " + str(i) + ", j = " + str(j) + ", lst = ")
                #print(lst)
                max_ij = 1
                for k in range(len(lst)):
                    if (k+1)*lst[k] > max_ij: 
                        max_ij = (k+1)*lst[k]
                matrix[i][j] = max_ij
        
        #print(matrix)
        #print(max(matrix))
        #return max(max(matrix))
        return max(max(x) for x in matrix)


