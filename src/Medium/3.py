# Algo. 1
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        : type s: str
        : rtype: int
        :
        : TC: 22.66%, best O(n), worst O(n^2)?
        : SC: 5.05%, about O(n)
        :\BF algo., use str_curr and str_longest to record the string of current, and the previous longest, and 
        : update accordingly. 
        """
        
        n_len = len(s)
        if n_len <= 1: return n_len
        
        str_curr    = []
        str_longest = []
        n_res       = 0
        
        for i in range(n_len):
            if s[i] not in str_curr:
                str_curr.append(s[i])
            else:
                idx = str_curr.index(s[i])
             
                if len(str_longest) < len(str_curr):
                    str_longest = str_curr.copy()
                    # if you use following assignment, and you use str_curr.append() or str_curr.pop()
                    # then it looks like str_longest and str_curr point exactly to the same var.
                    # if you assign by str_curr = ['a', 'b', 'c'], and str_longest = str_curr, then 
                    # it looks like str_longest and str_curr point to different vars. In general 
                    # it's safer and better to use str_longest = str_curr.copy()
                    # str_longest = str_curr
                for j in range(idx+1):
                    str_curr.pop(0)
                str_curr.append(s[i])
        
        # don't forget to compare the last str_curr.
        n_res = max(len(str_curr), len(str_longest))
        return n_res




