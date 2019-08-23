# Algo. 1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        : type nums: List[int]
        : rtype: List[List[int]]
        :
        : TC: 97.96%, O(n!*n)?, for n, we will have n! elements of list; 
        : SC: 5.36%, O(n*n!)?, 
        :\Algo. 1 from Ligang using recursion, which is a natural choice for this kind of problme. You need to define 
        : the recursive function inside to make it work.
        """
        n = len(nums)
        if n == 0: return []
        if n == 1: return [[nums[0]]]
        if n == 2: return [[nums[0], nums[1]], [nums[1], nums[0]]]
        
        def permute_helper(nums: List[int]):
            n = len(nums)
            # if n == 0: return []  # This end condition of course does NOT work!
            # if n == 1: return [[nums[0]]]  # This end condition also works! 
            # end condition, may be we can also use n==1?; if we just have n==0, the result will be all empty []? Yes!
            if n == 2: return [[nums[0], nums[1]], [nums[1], nums[0]]]
            
            lst_recu = permute_helper(nums[1:])
            # print(lst_recu)
            m = len(lst_recu)
            lst_res = []
            for i in range(m):  # (n-1)! elements, 
                # n positions, so it's n*(n-1)! = n!; 
                # Can also insert at the end!
                for j in range(len(lst_recu[i])+1):  
                    lst_elem = lst_recu[i].copy()
                    # print(lst_elem)
                    # lst_tmp = lst_elem.insert(j, nums[0])  # lst_tmp = None!!
                    lst_elem.insert(j, nums[0])
                    lst_res.append(lst_elem)
                #else:
                #    lst_elem = lst_recu[i].copy()
                #    # is it ok if lst_elem.insert(len(lst_recu[i]), nums[0]), i.e. insert at the end? Yes you can insert at the end!
                #    # actually if the inserting position >= len(lst_recu[i]), it all will insert at the end!
                #    # lst_tmp = lst_elem.append(nums[0])  # lst_tmp will None! insert and append functions do not return values!!
                #    lst_elem.append(nums[0])
                #    lst_res.append(lst_elem)
            
            return lst_res
        
        
        lst_res = permute_helper(nums)
        return lst_res

