# Algo. 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        : TC: 44.51%, O(n*logn) for sort,
        : SC: 6.25%, O(n) for dic, lst and lst_res, not so good
        : 
        :\1st idea, Hash Table to count the frequency with O(1) search, sort,
        :\Algo. 1 from Ligang using HashTable and python default sort. We may use heap sort to improve TC. 
        """
        dic = {}
        n = len(nums)
        for i in nums:
            if i not in dic: dic[i] = 1
            else: dic[i] +=1
        
        lst = []
        for ke in dic:
            lst.append([ke, dic[ke]])
        lst.sort(key=lambda elem: elem[1])
        
        lst_res = []
        nk = len(lst)
        # any better solution to extract the sub-array? need to use numpy? 
        for i in range(nk-k, nk):
            lst_res.append(lst[i][0])
        
        return lst_res




