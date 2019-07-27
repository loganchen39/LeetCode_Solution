class Solution:
    def threeSum(self, nums) -> List[List[int]]:
        """
        : type nums: List[int]
        : rtype: List[List[int]]
        :
        : TC: 65.37%, O((n/2)*(n/2)) = O(n^2)?
        : SC: 5.02%, O(n) for lst_res and dict_tmp
        :\BF algo., 4 cases, 3 zeros; 1 zero; two cases with no zero; Use dict as hash table like with
        : Two-Sum; If the final sum needs to be m, you can convert it to this problem, by subtracting 
        : m for all the list elements; 
        """
        
        n = len(nums)
        if n <= 2: return []
        if n == 3:
            if sum(nums) == 0: return [nums]  # not just nums!
            else: return []
        
        lst_res = []
        dict_tmp = {}
        
        # possible cases: 3 0s; 1 0 1 pos 1 neg; no 0 1 pos 2 neg or vice versa;
        if nums.count(0) >= 3: lst_res.append([0, 0, 0])
        
        if nums.count(0) >= 1: 
            for i in range(n):
                if nums[i] != 0:  # just like with Two-Sum; 
                    if -nums[i] not in dict_tmp:  # no need to be dict_tmp.keys()
                        dict_tmp[nums[i]] = i
                    else: 
                        # what if duplicated? will remove at the end; try to keep order; 
                        lst_res.append([-abs(nums[i]), 0, abs(nums[i])])  
        
        # how to remove all 0 in a list?
        nums.sort()
        if nums[0] >= 0 or nums[n-1] <= 0: return lst_res
        
        # then i_min_neg = 0; i_max_pos = n-1
        for i in range(n-1):
            if nums[i] < 0 and nums[i+1] >= 0: i_max_neg = i
            if nums[i] <= 0 and nums[i+1] > 0: i_min_pos = i+1; break
        
        # dict_tmp = {}  # need to put it inside the for-loop or it's wrong!!
        for i in range(i_max_neg+1):  # 1 neg 2 pos;
            s = -nums[i]
            dict_tmp = {}
            for j in range(i_min_pos, n):
                if s - nums[j] not in dict_tmp: dict_tmp[nums[j]] = j
                else: lst_res.append([nums[i], s-nums[j], nums[j]])
        
        for i in range(i_min_pos, n):  # 1 pos 2 neg;
            s = -nums[i]
            dict_tmp = {}
            for j in range(0, i_max_neg+1):
                if s - nums[j] not in dict_tmp: dict_tmp[nums[j]] = j
                else: 
                    lst_res.append([s-nums[j], nums[j], nums[i]])
        
        #\ERROR of "TypeError: unhashable type: 'list'"", how to remove duplicate?
        # The problem is that you can't use a mutable object (e.g. list) as the key in a dict or set,
        # you need to use immutable such as strings, numbers and tuples. 
        # The ERROR is complaining because there's no built-in hash function for lists (by design), and 
        # dictionaries are implemented as hash tables. 
        #\Sets require their items to be hashable. Out of types predefined by Python only the immutable 
        # ones, such as strings, numbers, and tuples, are hashable. Mutable types, such as lists and dicts, 
        # are not hashable because a change of their contents would change the hash and break the lookup code.
        #\Below is from: https://stackoverflow.com/questions/19371358/python-typeerror-unhashable-type-list/19371472
        #\Though tuples may seem similar to lists, they are often used in different situations and for 
        # different purposes. Tuples are immutable, and usually contain an heterogeneous sequence of elements 
        # that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the 
        # case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed 
        # by iterating over the list.
        #\Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can 
        # be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain 
        # only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, 
        # it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index 
        # assignments, slice assignments, or methods like append() and extend().
        
        # lst_res = list(set(lst_res)) 
        #\lst_res = [[1, 2], [3, 2, 1, 2], [2, 1]]
        # tmp = list(set(map(tuple, lst_res)))
        # print(tmp)  # the result is: [(1, 2), (3, 2, 1, 2), (2, 1)], so the order of each element matters!
        # and each element is a tuple, not a list, how come my following lst_res is ok? Each element becomes a list?
        lst_res = list(set(map(tuple, lst_res)))
        
        # anther way to convert back from tuple to list
        # result = map(list, sorted(set(map(tuple, my_list)), reverse=True))
        
        return lst_res




class Solution:
    def threeSum(self, nums):
        """
        : type nums: List[int]
        : rtype: List[List[int]]
        :
        : TC: 49.80%, O(n^2) for non-zero cases;
        : SC: 19.46%, O(n) for dict numsD and ans_set;
        :\BF algo., 4 cases, 3 zeros; 1 zero; two cases with no zero; Use dict as hash table for COUNTING like with
        : Two-Sum; list to dict (with counting), After poping all the zeros, the 2 non-zero cases can be combined and 
        : processed simply; 
        """
        
        n = len(nums)
        if n<3: return []
        if n == 3: return [] if sum(nums) else [nums]
        
        numsD = {}
        for i in nums:
            if i not in numsD:
                numsD[i] = 1
            else:
                numsD[i] +=1  # counting
                
        ans_set = set()
        
        if 0 in numsD:  # 2 cases with 0
            if numsD[0] >2:  # 3 zeros
                ans_set.add((0,0,0))
            numsD.pop(0)   # check all the dict functions
            for i in numsD.keys():  # 1 zero
                if -i in numsD:
                    i = abs(i)
                    ans_set.add((-i,0,i))  # keep order to avoid duplicate elements.
                    
        for i in numsD.keys():
            for j in numsD.keys():
                c = i+j
                if -c in numsD:
                    if (i == j and numsD[i]>1) or len({-c,i,j})==3:  # only these two cases.
                        temp = tuple(sorted([-c,i,j]))
                        ans_set.add(temp)
        
        # each element of the returned list is still a tuple, how come it's ok?  
        return list(ans_set)




