# Algo. 1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        :Do not return anything, modify nums in-place instead.
        :
        : TC: 7.31%, O(n**2) for 2 loops,
        : SC: 5.97%, O(1)
        :
        :\1st idea, loop from back to front, and move elements.
        :\Algo. 1 BF from Ligang, loop from back to front, and move element when encounters 0. 
        """
        nz = 0
        n = len(nums)
        i = n - 1
        while i >= 0 and nums[i] == 0: i -= 1
        if i <= 0: return
        
        idx_end = i
        while i >= 0:
            if nums[i] == 0:
                for j in range(i, idx_end):
                    nums[j] = nums[j+1]
                nums[idx_end] = 0
                idx_end -= 1
                
            i -= 1
        
        return




