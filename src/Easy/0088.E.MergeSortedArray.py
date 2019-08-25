# Algo. 1
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        TC: 14.39%, O(m+n) for the while loop.
        SC: 6.15%, O(1)
        
        Algo. 1, two pointers, be careful about how the pointers/indices change!
        """
        if n == 0: return
        #if m == 0: nums1 = nums2; return  # NOT working, while the next line works!
        if m == 0: nums1[0:n] = nums2[0:n]; return  # This is how you copy 1D array/list!
        #if m == 0:  # This also works;
        #    for i in range(n): nums1[i] = nums2[i]
        #    return
        
        if nums1[m-1] <= nums2[0]:
            nums1[m:m+n] = nums2[0:n]
            return
        if nums1[0] >= nums2[n-1]:
            nums1[n:n+m] = nums1[0:m]
            nums1[0:n]   = nums2[0:n]
            return
        
        
        i, j = 0, 0
        while j < n:
            k = i
            while k < m+j and nums1[k] < nums2[j]: k += 1
            if k == i: i = i  # this is how i changes!
            else: i += 1
                
            if k == m+j: 
                nums1[m+j:m+n] = nums2[j:n]
                return
            else: 
                for l in range(m+j, k, -1): nums1[l] = nums1[l-1]
                nums1[k] = nums2[j]
                # ums1.insert(k, nums2[j])  # WRONG! if so, then you will keep those 0s at the end;
                j += 1
                # i += 2  # WRONG! see above about how to set i!




