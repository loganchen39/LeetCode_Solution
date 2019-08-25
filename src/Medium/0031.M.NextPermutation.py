# Algo. 1
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        : Do not return anything, modify nums in-place instead.
        :
        : type nums: List[int]
        : rtype: None
        :
        : TC: 81.38%, worst case O(n^2) with 2 for-loops.
        : SC: 5.56%, 
        : 
        :\Algo. 1 BF from Ligang, make sure you understand the problem of "Next Greater Permutation", it's like
        : the "Least Bigger" or "Minimal Maximum", you start from the least significant bit (list element at index i), 
        : which is the right-end position, to find out the least bigger element afterward (here at index j), 
        : switch elements at i and j, then sort the partial list nums[i+1:n] in place in ascending order. 
        : so the new list will become the NEXT Greater Permutaiton.
        """
        n = len(nums)
        if n <= 1: return
        
        for i in range(n-2, -1, -1):
            i_least_bigger = float("inf")  # sys.maxsize, 1000000: they all work;
            j              = -1
            for j_idx in range(i+1, n):
                if nums[i] < nums[j_idx] and nums[j_idx] < i_least_bigger:
                    i_least_bigger = nums[j_idx]
                    j              = j_idx  # Do NOT forget this one!

            # this is a one-time thing, once found, after process, it will return!
            if i_least_bigger < float("inf"):  # sys.maxsize, 1000000: they all work;  
                tmp     = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                # NOR working, How to sort a list PARTIALLY and in-place? 
                # if nums is a numpy array, then the following code works.
                # nums[j:].sort()  
                #\it works, but it's NOT ALLOWED by requirement! No extra space!
                # if python does not provide such function, we need to write such function ourselves.
                lst_part = sorted(nums[i+1:n])  
                nums[i+1:n] = lst_part[:]  # for lst_part, with or without [:], both work; 
                return
        else:
            nums.reverse()

