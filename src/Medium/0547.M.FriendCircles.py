# Algo. 1
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        """
        : TC: 77.91%, O(n**4) worst cases, 4 for-loop?
        : SC: 5.88%, O(n) for lst_set, 
        :
        :\1st idea, combine/union sets, initialize n sets, use element to find the set?
        :\Algo. 1 BF from Ligang using 1st idea. Be aware there are several cases to consider! 
        : {0, 3}, {1, 2} then comes {2, 3} both 2 and 3 becomes empty, but they belong to different sets,
        : need to combine them; {0, 1}, {0, 2} then comes {1, 2}, both 1 and 2 are empty and they belong to
        : the same set {0, 1, 2}, 
        """
        n = len(M)
        i_res = n
        lst_set = []
        for i in range(n):
            lst_set.append({i})
        
        for i in range(n):
            for j in range(i+1, n):  # i < j, always.
                if M[i][j] == 1:
                    if lst_set[i] and lst_set[j]:
                        lst_set[i].add(j)
                        lst_set[j] = {}
                    elif lst_set[i] and not lst_set[j]:
                        for k in range(i):
                            if j in lst_set[k]:
                                lst_set[k] = lst_set[k].union(lst_set[i])
                                lst_set[i] = {}
                                break
                    elif not lst_set[i] and lst_set[j]:
                        for k in range(j):
                            if i in lst_set[k]:
                                lst_set[k] = lst_set[k].union(lst_set[j])
                                lst_set[j] = {}
                                break
                    else:  # not lst_set[i] and not lst_set[j], 
                        for k0 in range(i):
                            if i in lst_set[k0]:
                                break
                        for k1 in range(j):
                            if j in lst_set[k1]:
                                break
                        
                        k0, k1 = min(k0, k1), max(k0, k1)
                        if k0 != k1:  # combine the two sets, 
                            lst_set[k0] = lst_set[k0].union(lst_set[k1])
                            lst_set[k1] = {}
        
        lst_set = [set_elem for set_elem in lst_set if set_elem]  # list comprehension.
        return len(lst_set)




