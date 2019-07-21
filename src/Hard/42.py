class Solution:
    def trap(self, height):
        """
        : type height: List[int]
        : rtype: int
        :
        : TC: 5.07%, O(n^2)
        : SC: 5.10%, should be O(1), why so bad? 
        :\BF algo., You can look or abstract the problem at different perspectives, which will lead you to different
        : solutions. Here the idea is simple, for each idx, where the amount of water can be trapped is determined by
        : the minimal of the highest height at both left and right sides, which is exactly the "Approach 1" in LC Solution; 
        : The TC should be O(n^2), where inside of each for-loop, you need to find the maximum at both left and right side,
        : thus the TC is not good! There should be room for improvement, by avoiding checking maximum at both side all the time;
        :\
        """
        
        n = len(height)
        if n <= 2: return 0
        
        n_res  = 0
        n_curr = 0
        for i in range(1, n-1):
            max_left  = max(height[0  :i])
            max_right = max(height[i+1:n])
            min_lr    = min(max_left, max_right)
            if height[i] < min_lr:
                n_res += min_lr - height[i]
            
        return n_res




class Solution:
    def trap(self, height):
        """
        : type height: List[int]
        : rtype: int
        :
        : TC: 13.66%, O(n)
        : SC: 5.18%, O(n)
        :\DP algo. as in "Approach 2", Following the BF algo. as in "Approach 1", instead of computing the max_left and max_right for each idx repeatedly,
        : you can compute and store the max_left and max_right in one loop, thus the TC becomes O(n) which is a big improvement over 
        : the BF algo., 
        """
        
        n = len(height)
        if n <= 2: return 0
        
        n_res  = 0
        n_curr = 0
        
        max_left  = [0]*n
        max_right = [0]*n
        max_left[0]    = 0
        max_right[n-1] = 0
        
        # initialize and then loop to compute the max_left
        max_left[1] = height[0]
        for i in range(2, n):
            # Make sure you are crystal clear about the meaning of each var like the max_left[i-1]
            if height[i-1] > max_left[i-1]: max_left[i] = height[i-1]
            else: max_left[i] = max_left[i-1]
            
        max_right[n-2] = height[n-1]
        for i in range(n-3, -1, -1):
            if height[i+1] > max_right[i+1]: max_right[i] = height[i+1]
            else: max_right[i] = max_right[i+1]
        
        for i in range(1, n-1):
            min_h = min(max_left[i], max_right[i])
            if min_h > height[i]: n_res += min_h - height[i]
            
        return n_res
