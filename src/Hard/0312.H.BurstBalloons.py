# Algo.1 
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        :TC: O(n!)? Time Limit Exceeded with 28/70 test cases passed,
        :SC: O(?), recursion?!
        :
        :\1st idea, DP? recursion to try all cases? BF with TC O(n!) to try all cases; 
        :\For A.1, how do we know which "i" to choose that it's the optimal? A.1 is still 
        : like to try all cases, only with cache? Here we did not use cache, and it's
        : Time Limit Exceeded!
        """
        #n = len(nums)
        #if n == 0: return 0
        #if n == 1: return nums[0]
        #if n == 2: return nums[0]*nums[1]+a if a>=b else return nums[0]*nums[1]+b
    
        def dp(left, right):
            if left+1 == right: return 0
            
            max_res = -float("inf")
            for i in range(left+1, right):
                val = nums[left]*nums[i]*nums[right] + dp(left, i) + dp(i, right)
                if val > max_res: max_res = val
                    
            return max_res
        
        
        nums = [1] + nums + [1]
        n = len(nums)
        return dp(0, n-1)




