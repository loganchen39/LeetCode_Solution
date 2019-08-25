# Algo. 1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        : type height: List[int]
        : rtype: int
        :
        : TC: O(n^2), Time Limit Exceeded with 42/50 test cases passed.
        : SC: O(1), 
        :\Algo. 1 BF from Ligang, 2 for-loop to compute all possibilities, to get the maximum. Also
        : check my initial thought for the problem. 
        """
        n = len(height)
        # initial thought is that it should be DP or greedy algo. problem. you can NOT get rid of
        # the first SHORT bars because think about an extreme case which it has A LOT of short bars 
        # forward in the input array! It's not like a deterministic problem. It's an optimization
        # (maximum) and dynamic problem. 
        
        max_water = 0
        for i in range(1, n):
            for j in range(0, i):
                curr_water = (i-j)*min(height[j], height[i])
                if curr_water > max_water: max_water = curr_water
        
        return max_water




# Algo. 2
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        : type height: List[int]
        : rtype: int
        :
        : TC: O(n), 61.90%
        : SC: O(1), 5.31% (NOT correct?!)
        :\Algo. 2 Two Pointers as A2, check my initial thought in Algo. 1, where if you only look ONE-WAY FORWARD,
        : you will not be able to determine (check) what is in the last portion of the array! The Two Pointers 
        : set boundaries at both end sides, and check TWO-WAY towards INSIDE, to get the maximum result. 
        : BE AWARE that whether moving left or right pointer, depends on which side the height is shorter, so 
        : it will not miss the maximum. 
        """
        n = len(height)
        max_water = (n-1)*min(height[0], height[n-1])  # start from this initial value.
        
        l, r = 0, n-1
        while l < r:
            if height[l] <= height[r]: l += 1
            else: r -= 1
                
            curr_water = (r-l)*min(height[l], height[r])
            if curr_water > max_water: max_water = curr_water
        
        return max_water

