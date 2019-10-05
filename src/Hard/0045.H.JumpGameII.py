# Algo. 1
class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        :TC: NA, O(m0*m1*...*m(n-1)), recursion to try all cases, Time Limit Exceeded, with 65/92 test cases passed.
        :SC: NA, O(n) for recursion. 
        :
        :\1st idea, DP? How to convert the problem? Traceback with recursion to try all cases?
        : Algo. 1 BF from Ligang, recursion to try all cases, TC too bad, need to improve algo. by removing some redundent
        : cases. 
        """
        def recur_min_jump(idx: int, jumps: int, nums: List[int]) -> int:
            n = len(nums)
            if idx >= n: return -1
            #if idx == n-1: return 0
            if idx == n-1: return jumps  # base cases;
            
            if nums[idx] == 0: return -1  # stuck, will never be able to jump out, failed in this case
            
            min_jump = float("inf")
            for step in range(1, nums[idx]+1):
                n_jump = recur_min_jump(idx+step, jumps+1, nums)
                if 0 <= n_jump and n_jump < min_jump:
                    min_jump = n_jump
            
            if min_jump != float("inf"):
                return min_jump
            else: 
                return -1
        
        
        jumps = 0
        return recur_min_jump(0, jumps, nums)




class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        :TC: 65.92%, O(n)
        :SC: 8.33%, O(1)
        :
        :\Algo. 2 greedy by Ligang, the idea is simple, assume at position idx, it can jump 1 ~ nums[idx] steps, 
        : so the goal is to jump as "far" ("quick") as possible. Assume nums[idx] = 3, you gotta check that
        : after your next jump to (either) idx+1 ~ idx+3, you will have the furthest jump! Similar to check
        : the largest value of nums[idx+1 ~ idx+3]. This is local maximum problem, i.e. greedy algo.
        : You may think that, greedy is similar to find the LOCAL OPTIMAL (MAXIMUM or MINIMUM), and usually it's
        : one-way loop algo. (linear), while backtracking and recursion will try all cases/branches (non-linear 
        : tree structure); 
        """
        n        = len(nums)
        if n == 1: return 0
        
        jumps    = 0
        curr_idx = 0
        next_idx = 0
        
        # while curr_idx < n-1:
        while True:
            if curr_idx + nums[curr_idx] >= n-1:
                return jumps+1
            
            max_len = 0
            for i in range(1, nums[curr_idx]+1):
                if i + nums[curr_idx + i] > max_len: 
                    max_len  = i + nums[curr_idx+i]
                    next_idx = curr_idx + i
            
            if next_idx < n-1:
                curr_idx = next_idx
                jumps   += 1
            else:
                return jumps+1


