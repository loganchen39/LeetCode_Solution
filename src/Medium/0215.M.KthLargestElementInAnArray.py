# Algo. 1
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        : Input nums (List[int]): Description;
        : Input k (int): Description;
        : Output (int): Description;
        : 
        : TC: 80.67%, O(n*logn) for Tim-sort algo., may need to implement the sortig algo. myself!
        : SC: 10%, O(n) for Timsort, 
        :\Algo. 1 BF from Ligang, simple idea of first sort and then get the result. It can NOT be 
        : what the interviewer want! Must check other LC solutions.
        """
        n = len(nums)
        if n == 0: return None
        
        nums.sort()
        return nums[n-k]

