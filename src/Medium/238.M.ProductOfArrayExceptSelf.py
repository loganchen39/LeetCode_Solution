# Algo. 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        : type nums: List[int]
        : rtype: List[int]
        :
        : TC: O(n), 91.23%, 
        : SC: O(n) for lst_res, 75.57%, 
        :\Algo. 1 using division which is actually NOT allowed! Need to check and implement LC solutions! 
        """
        n = len(nums)  # n>=2
        n_zero = nums.count(0)
        if n_zero >= 2: return [0]*n
        
        pdt = 1
        for i in range(n):
            if nums[i] != 0: pdt = pdt*nums[i]
        
        lst_res = [1]*n
        if not n_zero: 
            for i in range(n): lst_res[i] = int(pdt/nums[i])
        else:
            for i in range(n):
                # SyntaxError: can't assign to conditional expression
                # lst_res[i] = pdt  if nums[i] == 0 else lst_res[i] = 0  
                if nums[i] == 0: lst_res[i] = pdt
                else: lst_res[i] = 0 
                
        return lst_res


