# Algo. 1
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        : TC: 5.08%, O(n*n*M), n being the length of list words, and M being the length of each single word, 
        : SC: 100%, O(n) for dic, 
        : 
        :\1st idea, first it should be a good idea to sort the list according to the length of the words.
        : then use backtracking to find the maximum length of the string chain? For each word, we can also 
        : record it's maximum lengh of string chain (which starts with the word), it's like bottom-up DP. 
        : When trying to implement the recursive backtracking function, for each current word, there are
        : multiple paths, and you want to find the maximum length, how to compute or store this maximum 
        : length through the recursive function? Meanwhile you will need to compute the maximum length for
        : each word on the path (even it's not the path with maximum length), how do you store the record
        : for later use as bottom-up DP programming? 
        :\Algo. 1 from discuss "easy peasy python solution using map", implemented by Ligang, the key point
        : here is that, after sorting, you process the word from longest (last) to shortest (first), because 
        : you can determine the maximum length of the longest (last) words easily, and gradually compute
        : backward, you'll get the final dic[words[i]], which initially I want to use "lst_max_len = [-1]*n"
        : to store. No need for recursion! If you start with processing the shortest words, you'll have 
        : the above problems with recursion.
        """
        def isPredecessor(wd0, wd1) -> bool:
            if len(wd1) != len(wd0)+1: return False
            n = len(wd1)
            for i in range(n):
                str_tmp = wd1[0:i] + wd1[i+1:n]
                if str_tmp == wd0: 
                    return True
            return False
        
        
        n = len(words)
        words.sort(key=lambda wd: len(wd))
        # lst_max_len = [-1] * n
        dic = {}
        for i in range(n-1, -1, -1):
            max_len = 1
            for wd in dic:
                if isPredecessor(words[i], wd):
                    if dic[wd] + 1 > max_len: 
                        max_len = dic[wd] + 1
            dic[words[i]] = max_len
        
        return max(dic.values())
        
        
        
        ## not used, too complicated if you start with processing the shortest words with recursion.
        #def bt_max_len(words, i, cnt):
        #    if lst_max_len[i] != -1: return lst_max_len[i]
            
        #    n = len(words)
        #    if i == n-1: return 1
            
        #    b_noPostdecessor = True
        #    curr_max_len = 1
        #    for j in range(i+1, n):
        #        if len(words[j]) >= len(words[i])+2: break
        #        if isPredecessor(words[i], words[j]):
        #            b_noPostdecessor = False
        #            length = bt_max_len(words, j, cnt+1)
                    
        #    if b_noPostecessor:
        #        return cnt




