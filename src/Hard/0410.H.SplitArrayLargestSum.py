class Solution:
    def __init__(self):
        self.globalMax = float("inf")
        
        
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        : TC: NA, O(n^m), TLE with 14/27 test cases passed;
        : SC: NA, O(n) for recursion?
        :
        :\1st idea, DP? 
        : Algo. 1 from A.1 B.F., use recursion (backtrace?) to try ALL CASES to find the minimal maximum. 
        : The recursion here is UNUSUAL as it will try ALL numSubarrays from 0, 1, 2, ..., m! 
        : Here we use class member var self.globalMax (or you can use a global var) to record the result
        : of minimal maximum. The recursive function parameters are like "constants".
        """
        def dfs(nums, m, i, numSubarrays, currSum, currMax):
            n = len(nums)
            
            if i == n and numSubarrays == m:
                self.globalMax = min(self.globalMax, currMax)
                return
            
            if i == n:
                return
            
            # ? can not be "if i >= 0", can be "if numSubarrays >= 1:";
            # Because in the begining, it's initialized as: i=0, numSubarrays=0, 
            if i > 0:  
                dfs(nums, m, i+1, numSubarrays  , currSum + nums[i], max(currMax, currSum+nums[i]))
            if numSubarrays < m:
                # This will run first when i==0; 
                dfs(nums, m, i+1, numSubarrays+1, nums[i]          , max(currMax, nums[i]        ))
        
        
        dfs(nums, m, 0, 0, 0, 0)
        
        return self.globalMax




# Algo. 2
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        : TC: NA, O(n*n*m), TLE with 26/27 test cases passed;
        : SC: NA, O(n*m)
        :
        : Algo. 2 from A.2, Need to understand later. 
        """
        n = len(nums)
        f = [[float("inf")]*(m+1) for i in range(n+1)]  # f[n+1][m+1]
        
        sub = [0]*(n+1)
        for i in range(n): 
            sub[i+1] = sub[i] + nums[i]
        
        f[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(0, i):
                    f[i][j] = min(f[i][j], max(f[k][j-1], sub[i] - sub[k]))
        
        return f[n][m]




