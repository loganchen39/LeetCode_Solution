# Algo. 1, WRONG understanding of the problem, 
# for input {"bbaa", "aba"}, my output is "ba", expected output is "baa"!
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        : type s: str
        : type t: str
        : rtype: str
        :
        : TC:
        : SC:
        :\
        """
        # t = str(set(t))  # WRONG, t = "{'B', 'C', 'A'}", t_set = set(t) = {'{', 'C', '}', 'B', "'", ',', ' ', 'A'} 
        ns, nt = len(s), len(t)
        s_set = set(s)
        t_set = set(t)    
        if not (t_set <= s_set) or ns < nt: return ""
        if nt == ns: return s
        
        nt = len(t_set)
        
        min_len  = float("inf")
        curr_len = 0
        dict_idx = dict()
        str_res = ""
        
        p0 = 0
        while p0 < ns and (s[p0] not in t): p0 += 1
        p1 = p0
        while p1 < ns:
            if s[p1] in t: 
                if s[p1] not in dict_idx: 
                    dict_idx[s[p1]] = [p1]
                    if len(dict_idx) == nt: 
                        min_len = curr_len = p1 - p0 + 1
                        str_res = s[p0:p1+1]
                        break
                else: dict_idx[s[p1]].append(p1) 
            p1 += 1
            
        print("p0 = " + str(p0) + ", p1 = " + str(p1))
        if min_len == nt: return s[p0:p1+1]
        
        while p1 < ns and p0 <= p1:
            ch = s[p0]
            if ch in s[p0+1: p1+1]:
                p0 += 1
                while s[p0] not in t: p0 += 1  # new p0 which is valid s[p0:p1+1]
            else: 
                if ch not in s[p1:]: 
                    if p1 - p0 + 1 < min_len:
                        min_len = p1 - p0 + 1
                        str_res = s[p0:p1+1]
                    return str_res
                else:
                    p1 += 1
                    while s[p1] != ch: p1 += 1
                    p0 += 1
                    while s[p0] not in t: p0 += 1
                    
                    if p1 - p0 + 1 < min_len:
                        min_len = p1 - p0 + 1
                        str_res = s[p0:p1+1]




# Algo. 2
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        : type s: str
        : type t: str
        : rtype: str
        :
        : TC: O(n)?, 5.37%, while-loop with str.count(), O(n^2)?
        : SC: O(m+n), 7.72%, for additional dict and set.
        :\Algo. 2 Sliding window with Two-Pointers p0 and p1 similar to Approach 1, anytime (p0, p1) is valid 
        : which means s[p0:p1+1] contains all of t characters. Moving p0 or p1 to find the minimum valid window. 
        : Previously my understanding of the problem is wrong! For input {"bbaa", "aba"}, my previous output 
        : is "ba", expected output is "baa", it needs to contain 2 'a's to be valid, the number of a character
        : counts! Then we can use Hashtable to store the number of characters. 
        """
        # FIRST handle special cases, normally with no valid window, and return ""
        # WRONG, t = "{'B', 'C', 'A'}", t_set = set(t) = {'{', 'C', '}', 'B', "'", ',', ' ', 'A'} 
        # t = str(set(t))  
        ns, nt = len(s), len(t)
        s_set = set(s)
        t_set = set(t)    
        # "t_set > s_set" not equal to "not t_set <= s_set"!! Unlike integer comparison, set can be joint and overlap!
        if not (t_set <= s_set) or nt > ns: return ""  
        # if nt == ns: return s
        
        dict_s = dict()
        dict_t = {}
        
        for i in range(ns):
            if s[i] not in dict_s: dict_s[s[i]] = 1
            else: dict_s[s[i]] += 1
        for i in range(nt):
            if t[i] not in dict_t: dict_t[t[i]] = 1
            else: dict_t[t[i]] += 1
        for ch in dict_t:
            if dict_t[ch] > dict_s[ch]: return ""
        
        
        min_len  = float("inf")
        curr_len = 0
        dict_sw  = dict()
        str_res  = ""
        
        # SECOND find the initial valid window
        p0 = 0
        while p0 < ns and (s[p0] not in t): p0 += 1
        p1 = p0
        while p1 < ns:
            if s[p1] in t: 
                if s[p1] not in dict_sw: 
                    dict_sw[s[p1]] = 1
                else: 
                    dict_sw[s[p1]] += 1
                
                if len(dict_sw) == len(dict_t):
                    for ch in dict_t:
                        if dict_sw[ch] < dict_t[ch]: break  # break for-loop
                    else: break  # break while-loop?                     
            p1 += 1
            
            
        # print("p0 = " + str(p0) + ", p1 = " + str(p1))
        min_len = p1 - p0 + 1
        str_res = s[p0:p1+1]
        if min_len == nt: return str_res
        
        # THIRD sliding window (moving p0 or p1) to find the minimum window.
        while p1 < ns and p0 <= p1:
            ch = s[p0]
            
            if s[p0+1:p1+1].count(ch) >= dict_t[ch]:  # moving p0
                p0 += 1
                while s[p0] not in dict_t and p0 <= p1: p0 += 1
                    
                if p1 - p0 + 1 < min_len:
                    min_len = p1 - p0 + 1
                    str_res = s[p0:p1+1]
                    if min_len <= nt: return str_res
            else:  # moving p1
                if ch not in s[p1+1:]:
                    if p1 - p0 + 1 < min_len:
                        min_len = p1 - p0 + 1
                        str_res = s[p0:p1+1]
                    return str_res
                else:
                    p1 += 1
                    while s[p1] != ch: p1 += 1
                    p0 += 1
                    while s[p0] not in t: p0 += 1
                    
                    if p1 - p0 + 1 < min_len:
                        min_len = p1 - p0 + 1
                        str_res = s[p0:p1+1]
                        if min_len <= nt: return str_res


