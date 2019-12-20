# Algo. 1
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        :
        : TC: 69.83%, O(m*logn) or O(n*logm) worst case,
        : SC: 7.41%, O(1), 
        : 
        :\1st idea, sth like heap sort? 
        :\Algo. 1 BF binary search for sorted array from Ligang, any better solutions for this 2-way ascending 
        : matrix?
        """
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False
        
        # binary search for each row
        for i in range(m):
            if matrix[i][0] > target or matrix[i][n-1] < target: 
                continue
                
            l, h = 0, n-1
            while (l <= h):
                mid = int((l+h)/2)
                if matrix[i][mid] == target: return True
                elif matrix[i][mid] < target: l = mid + 1
                else: h = mid - 1
            
        return False




