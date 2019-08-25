# Algo. 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        : type strs: List[str]
        : rtype: List[List[str]]
        :
        : TC: O(n^2*k), n being # of strs, k being length of a string, Time Limit Exceeded with 100/101 test cases passed.
        : SC: O(n) (for lst_res) + O(k) for set and dict in function isequal. ?
        :\Algo. 1 BF from Ligang, 2 for-loop to check and process. Defined a function to compare 2 strings
        : to see if they are "equal". The TC should be an issue, any better algo.?
        """
        def isequal(str1, str2):
            n1, n2 = len(str1), len(str2)
            if n1 != n2: return False
            
            s1, s2 = set(str1), set(str2)
            if s1 != s2: return False
            
            d1, d2 = dict(), {}
            for i in range(n1):
                if str1[i] not in d1: d1[str1[i]] = 1
                else: d1[str1[i]] += 1
            for i in range(n2):
                if str2[i] not in d2: d2[str2[i]] = 1
                else: d2[str2[i]] += 1
                
            for ch in d1:
                if d1[ch] != d2[ch]: return False
            
            return True
        
        
        n = len(strs)
        if n <= 1: return [strs]
        
        lst_res = []
        for i in range(n):
            n_tmp = len(lst_res)
            for j in range(n_tmp):
                if isequal(strs[i], lst_res[j][0]): 
                    lst_res[j].append(strs[i])
                    break
            else:
                lst_res.append([strs[i]])
        
        return lst_res




# Algo. 2
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        : type strs: List[str]
        : rtype: List[List[str]]
        :
        : TC: O(n*k*logk), 74.10%, n being # of strs, k being length of a string
        : SC: O(n), 20.04%, for dict, 
        :\Algo. 2 as A1 Categorize by Sorted String, this kind of Group/Categorize problem is like a
        : mathematical mapping, where Dictionary should be a perfect data structure. Here we should 
        : be able to think of the key as tuple(sorted(strs[i])). Compared to Algo. 1 BF with 2 for-loop,
        : you will find the key in the Dict in constant time with the sorted tuple, no need to determine
        : if the two strings are equal with the self-defined function isequal() anymore. 
        """
        n = len(strs)
        if n <= 1: return [strs]
        
        # difference with: d = collections.defaultdict(list) ? 
        d = dict()
        
        for i in range(n):
            tup = tuple(sorted(strs[i]))
            if tup not in d: d[tup] = [strs[i]]
            else: d[tup].append(strs[i])
        
        # type(d.values()) is <class 'dict_values'>, not a list.
        return list(d.values())


