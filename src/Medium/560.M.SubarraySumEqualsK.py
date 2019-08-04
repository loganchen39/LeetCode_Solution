# Algo. 1
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        : type nums: List[int]
        : type k: int
        : rtype: int
        :
        : TC: O(n^3), Time Limit Exceeded with 58/80 test cases passed. 2 for-loop and the "sum" function combine to be O(n^3)
        : SC: O(1)
        :\Algo. 1 BF from Ligang as A1, 2 for-loop to check all subarrays, TC bad. 
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1:
            if nums[0] == k: return 1
            else: return 0
        
        n_res = 0
        for i in range(n):
            for j in range(i, n):
                if sum(nums[i:j+1]) == k: n_res += 1
        
        return n_res




# Algo. 2
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        : type nums: List[int]
        : type k: int
        : rtype: int
        :
        : TC: O(n^2), Time Limit Exceeded with 58/80 test cases passed. 2 for-loop, with help from a cumulative sum.
        : SC: O(n) for cumulative sum lst_subsum.
        :\Algo. 2 Using cumulative sum as A2, 2 for-loop, we should always consider this cumulative sum for these
        : "continuous subarray sum". 
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1:
            if nums[0] == k: return 1
            else: return 0
        
        n_res = 0
        
        lst_subsum = [nums[0]]
        for i in range(1, n):
            lst_subsum.append(lst_subsum[i-1] + nums[i])
        
        for i in range(n):
            for j in range(i, n):
                # check sum of [i:j] inclusive, or sum(nums[i:j+1]).
                if i == 0: 
                    if lst_subsum[j] == k: n_res += 1
                else:
                    if lst_subsum[j] - lst_subsum[i-1] == k: n_res += 1
                
        return n_res




# Algo. 3
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        : type nums: List[int]
        : type k: int
        : rtype: int
        :
        : TC: O(n), 70.13%
        : SC: O(n), 20.92%, for cumulative sum lst_subsum and dict.
        :\Algo. 3 Using cumulative sum and HashTable as A4, we should always consider this cumulative sum for these
        : "continuous subarray sum". Here the key to use HashTable is, it should be within the same for-loop, 
        : so for the current subsum, you can check with the "previous" subsum results, in O(1) TC. If you 
        : create and use the HashTable in a new for-loop like I did initially, you will not have the "order"
        : of "previous" subsum info. It's about how you store and process the data in an appropriate order and manner. 
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1:
            if nums[0] == k: return 1
            else: return 0
        
        n_res = 0
        
        d = {}
        lst_subsum = [nums[0]]  # actually no need for this list, waste of space!
        # do NOT forget this case! One way to avoid this is to initialize lst_subsum = [0] with an extra 0. 
        if nums[0] == k: n_res += 1  
        d[nums[0]] = 1
        for i in range(1, n):
            subsum = lst_subsum[i-1] + nums[i]
            lst_subsum.append(subsum)
            
            if subsum == k: n_res += 1
            if subsum-k in d: n_res += d[subsum-k]
            
            if subsum not in d: d[subsum] = 1
            else: d[subsum] += 1
             
        # d = {}
        #for i in range(n):
        #    if lst_subsum[i] not in d: d[lst_subsum[i]] = 1
        #    else: d[lst_subsum[i]] += 1
             
        return n_res




# Algo. 3
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        : type nums: List[int]
        : type k: int
        : rtype: int
        :
        : TC: O(n), 70.13%
        : SC: O(n), 20.92%, for cumulative sum lst_subsum and dict.
        :\Still Algo. 3, set an extra 0 at the beginning of lst_subsum, to simply coding. 
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1:
            if nums[0] == k: return 1
            else: return 0
        
        n_res = 0  
        d = {}
        lst_subsum = [0] 
        d[0] = 1
        for i in range(0, n):
            subsum = lst_subsum[i] + nums[i]
            lst_subsum.append(subsum)
            
            # if subsum == k: n_res += 1  # no need for this anymore. 
            if subsum-k in d: n_res += d[subsum-k]
            
            if subsum not in d: d[subsum] = 1
            else: d[subsum] += 1

        return n_res


