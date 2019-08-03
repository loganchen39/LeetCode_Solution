# Algo. 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        : type nums: List[int]
        : type target: int
        : rtype: int
        : 
        : TC: O(logn), 98.80%, binary search
        : SC: O(1), 5.13% (NOT correct!?)
        :\Algo. 1 of Ligang, 2 binary searches first to find the index of minimum element, then to find the
        : target, within the appropriate sub-segment. Similar to A1. 
        """
        n = len(nums)
        if n == 0: return -1
        if n == 1:
            # return 0 if nums[0] == target else return -1  # invalid syntax
            if nums[0] == target: return 0
            else: return -1
        
        # find the index of minimum element
        if nums[0] < nums[n-1]: idx_min = 0
        else:
            low, high = 0, n-1
            while low <= high:
                mid = int((low+high)/2)
                if mid>=1 and mid<=n-2:
                    if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                        idx_min = mid
                        break
                    else:
                        if nums[mid] > nums[0]: low = mid + 1
                        else: high = mid - 1
                elif mid == 0:
                    if nums[mid] > nums[mid+1]: idx_min = mid + 1
                    break
                elif mid == n-1:
                    if nums[mid] < nums[mid-1]: idx_min = n-1
                    break
        
        # print("idx_min = " + str(idx_min))
        
        if idx_min == 0: 
            idx_st, idx_end = 0, n-1
        elif target >= nums[0]:
            idx_st, idx_end = 0, idx_min - 1
        else:
            idx_st, idx_end = idx_min, n-1
            
        # print("idx_st = " + str(idx_st) + ", idx_end = " + str(idx_end))
        
        if idx_end == idx_st:
            if nums[idx_st] != target: return -1
            else: return idx_st
        
        if target < nums[idx_st] or target > nums[idx_end]: return -1
        
        low, high = idx_st, idx_end
        while low <= high:
            mid = int((low+high)/2)
            if nums[mid] == target: return mid
            elif nums[mid] < target: low = mid + 1
            else: high = mid - 1
            
        return -1