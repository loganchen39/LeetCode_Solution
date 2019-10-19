# Algo. 1
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        """
        : TC: 90.17%, O(7n)=O(n), 
        : SC: 14.29%, O(1), 
        :
        :\1st idea, check if there is a number that exists at all (A[i], B[i]), i = 0, ..., n-1,
        : if there is (say m), count the number from A or B which has less number of m, which should
        : be the result. If there is not, then retur -1. Not DP, relatively easier. BE AWARE that 
        : A[i] can be equal to B[i]! Consider the test case 68:
        : [1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]
        :\Algo. 1 as the 1st idea, implemented by Ligang. 
        """
        n = len(A)
        if n <= 1: return 0
        
        m_arr = [-1]*2
        idx   = 0
        for i in range(1, 7):
            for j in range(n):
                if i not in (A[j], B[j]):
                    break
            else:  # if it breaked above, this "else" will not be executed!
                m_arr[idx] = i
                idx       += 1
                
        print("idx = " + str(idx))
        print(m_arr)
        
        if idx == 0: return -1
        
        if idx == 2:
            n_m0 = A.count(m_arr[0])
            n_m1 = B.count(m_arr[0])
            return min(n_m0, n_m1, n-n_m0, n-n_m1)
        
        # idx == 1
        n_m0 = A.count(m_arr[0])
        n_m1 = B.count(m_arr[0])  # this is necessary as A[i] can be equal to B[i]!
        return min(n_m0, n-n_m0, n_m1, n-n_m1)




