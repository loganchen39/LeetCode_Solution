# Algo. 1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        : Input:
        : nums (List[int]): Description;
        : Output (int): Description
        :
        : TC: 59.63%, Timsort, Average O(n*logn), 
        : SC: 8.70%, Timsort, Average O(n), The TC and SC do not satisfy the requirement! Need better algo.
        :\Algo. 1 BF from Ligang, first sort and then check, starting from 1; 
        """
        n = len(nums)
        if n == 0: return 1
        if n == 1: 
            if nums[0] == 1: return 2
            else: return 1
            
        nums.sort()
        smpi = 1
        for i in range(n):
            if nums[i] == smpi: smpi += 1
            elif nums[i] > smpi: return smpi
        else:
            return smpi




# Algo. 2
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        : Input:
        : nums (List[int]): Description;
        : Output (int): Description
        :
        : TC: 84.84%, O(n), 
        : SC: 8.70%, O(n), SC does not satisfy the requirement! Need better algo.
        :\Algo. 2 BF from Ligang, use Hash Set; 
        """
        n = len(nums)
        if n == 0: return 1
        if n == 1: 
            if nums[0] == 1: return 2
            else: return 1
            
        set_pi = set()
        for i in range(n):
            if nums[i] > 0: set_pi.add(nums[i])
        for i in range(1, len(set_pi)+2):
            if i not in set_pi: return i




# Algo. 3
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        : Input:
        : nums (List[int]): Description;
        : Output (int): Description
        :
        : TC: 97.45%, O(n), 
        : SC: 8.70%, O(1), 
        :\Algo. 3 from solution 1, take advantage of the nums, and set flags etc. in place, a little tricky.
        """
        n = len(nums)
        if n == 0: return 1
        if n == 1: 
            if nums[0] == 1: return 2
            else: return 1
        
        if 1 not in nums: 
            return 1
        else: 
            for i in range(n):
                if nums[i] <= 0 or nums[i] >= n+1:
                    nums[i] = 1
        
        if nums[0] < n:
            if nums[nums[0]] > 0:
                nums[nums[0]] = -nums[nums[0]]
        else:
            nums[0] = -nums[0]
            
        for i in range(1, n):
            if abs(nums[i]) == n:
                if nums[0] > 0: 
                    nums[0] = -nums[0]
            elif nums[abs(nums[i])] > 0: 
                nums[abs(nums[i])] = -nums[abs(nums[i])]
        
        print(nums)
                
        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0: return n
        
        return n+1

