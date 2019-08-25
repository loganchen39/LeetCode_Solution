# Algo. 1
import sys
class Solution:
    def maxSubArray(self, nums):
        """
        : type nums: List[int]
        : rtype: int
        :
        : TC: O(n^3), Time Limit Exceeded, with 200/202 test cases passed, 
        : SC: O(1)
        :\BF algo., 2 for-loop to check all the subarrays, to find the maximum. 
        """
        
        n = len(nums)
        if n==1: return nums[0]
        if n==2:
            # max(iterable, *[, key, default])
            # max(arg1, arg2, *args[, key])
            # Return the largest item in an iterable or the largest of two or more arguments.
            return max(nums[0], nums[1], nums[0]+nums[1])
        
        # n_res = float('-inf')
        n_res = -sys.maxsize
        for i in range(n):
            for j in range(i+1, n+1):  # j can be n, so it should be n+1; 
                s = sum(nums[i:j])
                if s > n_res: n_res = s
        
        return n_res




# Algo. 2
import sys
class Solution:
    def maxSubArray(self, nums):
        """
        : type nums: List[int]
        : rtype: int
        :
        : TC: O(n^2), Time Limit Exceeded, with 200/202 test cases passed, 
        : SC: O(n)
        :\Algo. 2, with subsum, 2 for-loop to check all the subarrays, to find the maximum. 
        """
        
        n = len(nums)
        if n==1: return nums[0]
        if n==2: return max(nums[0], nums[1], nums[0]+nums[1])
        
        subsum = [0] + [sum(nums[0:i+1]) for i in range(n)]  # can be optimized with a loop to accumulate.
        n_res = -sys.maxsize
        for i in range(0, n):
            for j in range(i+1, n+1):
                if subsum[j]-subsum[i] > n_res: n_res = subsum[j]-subsum[i]

        return n_res




# Algo 3;
class Solution:
    def maxSubArray(self, nums):
        """
        : type nums: List[int]
        : rtype: int
        :
        : TC: O(n), 50.19%
        : SC: O(1), 5.02%, NOT correct?!: 
        :\Algo. 3 of DP as in Approach 3, the idea is to modify nums[n] to compute a LOCAL max sum array, 
        : to get the GLOBAL max sum. For the local max sum at index i, if nums[i-1]<0, then restart and reset
        : it as nums[i], otherwise set it as nums[i] = nums[i-1] + nums[i]; 
        """
        
        n = len(nums)
        if n==1: return nums[0]
        if n==2: return max(nums[0], nums[1], nums[0]+nums[1])
        
        g_max_sum = nums[0]
        idx_st    = 0
        for i in range(1, n):
            if nums[i-1] < 0: idx_st = i
            else: nums[i] += nums[i-1]
                
            if nums[i] > g_max_sum: g_max_sum = nums[i]

        return g_max_sum




# Algo. 4
class Solution:
    def maxSubArray(self, nums):
        """
        : type nums: List[int]
        : rtype: int
        :
        : TC: O(nlogn ?), 5.83%
        : SC: O(logn ?) to keep the recursion stack, 5.02%, NOT correct?!: 
        :\Algo. 4 of Divide and Conquer as in Approach 1, the KEY idea lies in computing the cross_sum, which
        : MUST INCLUDE the end element of left subarray, and the start element of right subarray. Think like 
        : this, if the result global max subarray does not include either one, then the result global max subarray
        : will be in either the left subarray or the right subarray. So it only has these 3 cases: left, right, cross;
        """
        def cross_sum(nums, l, r, p):
            """
            : Then the result of cross_sum is the sum of max left subarray which start from the index p (going back to left)
            : and of right subarry which start from the index p+1 (going forward to right).
            : TC is O(r-l), SC is O(1)
            """
            if l == r: return nums[l]
            
            l_max_sum = float('-inf')
            curr_sum = 0
            for i in range(p, l-1, -1):
                curr_sum += nums[i]
                if l_max_sum < curr_sum: l_max_sum = curr_sum
            
            r_max_sum = float('-inf')
            curr_sum  = 0
            for i in range(p+1, r+1):
                curr_sum += nums[i]
                if r_max_sum < curr_sum: r_max_sum = curr_sum
            
            return l_max_sum + r_max_sum
        
        
        def helper(nums, l, r):
            # if a function is defined inside another function like this one, you do NOT need to use self!?; 
            # otherwise you will need to, like the code below with the same algo.
            if l == r: return nums[l]  # final returning condition
            
            p = int((l+r)/2)
            l_sum = helper(nums, l, p)
            r_sum = helper(nums, p+1, r)
            c_sum = cross_sum(nums, l, r, p)
            
            return max(l_sum, r_sum, c_sum)
        
        
        n = len(nums)
        if n==1: return nums[0]
        if n==2: return max(nums[0], nums[1], nums[0]+nums[1])
        
        return helper(nums, 0, len(nums)-1)




# Algo. 4 same as above, with some helper functions defined outside.
class Solution:
    def cross_sum(self, nums, l, r, p):
        """
        :\This comment also needs to be indented like this!
        :\Then the result of cross_sum is the sum of max left subarray which start from the index p (going back to left)
        : and of right subarry which start from the index p+1 (going forward to right).
        : TC is O(r-l), SC is O(1)
        """
        if l == r: return nums[l]
            
        l_max_sum = float('-inf')
        curr_sum = 0
        for i in range(p, l-1, -1):
            curr_sum += nums[i]
            if l_max_sum < curr_sum: l_max_sum = curr_sum
            
        r_max_sum = float('-inf')
        curr_sum  = 0
        for i in range(p+1, r+1):
            curr_sum += nums[i]
            if r_max_sum < curr_sum: r_max_sum = curr_sum
            
        return l_max_sum + r_max_sum
    
    
    def helper(self, nums, l, r):
        # if a function is defined inside another function like this one, you do NOT need to use self!?; 
        # otherwise you will need to. 
        if l == r: return nums[l]  # final returning condition
            
        p = int((l+r)/2)
        l_sum = self.helper(nums, l, p)
        r_sum = self.helper(nums, p+1, r)
        c_sum = self.cross_sum(nums, l, r, p)
            
        return max(l_sum, r_sum, c_sum)
        
        
    def maxSubArray(self, nums):
        """
        : type nums: List[int]
        : rtype: int
        :
        : TC: O(nlogn ?), 5.83%
        : SC: O(logn ?), to keep the recursion stack, 5.02%, NOT correct?!: 
        :\Algo. 4 of Divide and Conquer as in Approach 1, the KEY idea lies in computing the cross_sum, which
        : MUST INCLUDE the end element of left subarray, and the start element of right subarray. Think like 
        : this, if the result global max subarray does not include either one, then the result global max subarray
        : will be in either the left subarray or the right subarray. So it only has these 3 cases: left, right, cross;
        """
        #n = len(nums)
        #if n==1: return nums[0]
        #if n==2: return max(nums[0], nums[1], nums[0]+nums[1])
        
        return self.helper(nums, 0, len(nums)-1)



# Algo. 5
class Solution:
    def maxSubArray(self, nums):
        """
        : type nums: List[int]
        : rtype: int
        :
        : TC: O(n), 50.19%
        : SC: O(1), 5.02%, NOT correct!?: 
        :\Algo. 5 of Greedy as in Approach 2, it's similar to Algo. 4 of DP as in Approach 3. The idea is to always 
        : pick the locally optimal move at each step, and that will lead to the globally optimal solution; 
        """
        n = len(nums)
        if n==1: return nums[0]
        if n==2: return max(nums[0], nums[1], nums[0]+nums[1])
        
        curr_sum = max_sum = nums[0]
        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum+nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum




# Algo. 6
class Solution:
    def maxSubArray(self, nums):
        """
        : type nums: List[int]
        : rtype: int
        :
        : TC: O(n)
        : SC: O(1)
        :\Algo. 6. FAILED, try to deal with different cases, which is too complicated to make it correct!
        : As checked with Approach 3 of DP, they are somewhat similar with ideas.
        """
        
        n = len(nums)
        if n==1: return nums[0]
        if n==2: return max(nums[0], nums[1], nums[0]+nums[1])
        
        prev_sum = nums[0]
        idx_st   = 0
        idx_ed   = 0
        for i in range(1, n):
            if prev_sum < 0: 
                if nums[i] >= 0:         prev_sum = nums[i]; idx_st = i; idx_ed = i
                elif nums[i] > prev_sum: prev_sum = nums[i]; idx_st = i; idx_en = i
                else: pass
            else: 
                if nums[i] < 0: pass
                else:
                    if sum(nums[idx_st:i]) < 0: prev_sum = nums[i]; idx_st = i; idx_ed = i
                    elif prev_sum > sum(nums[idx_st:i]): pass
                    else: prev_sum += nums[i]; idx_ed = i

        return prev_sum
