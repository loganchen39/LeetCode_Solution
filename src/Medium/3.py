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




# Algo. 2
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        : type s: str
        : rtype: int
        :
        : TC: 33.69%, best O(n), worst O(n**2)?
        : TC: 33.69%, O(2n) (worst case) = O(n); 
        : SC: 5.05%, Best O(1), worst O(n) for dict, average should be O(n)?
        : SC: 5.05%, O(min(m,n)), the size of the Set is upper bounded by n and the size of charset m; 
        :\Algo. Sliding window with Two-Pointers and hashtable, the pointers are more facile or lightweighted to use.
        : This is the same algo. as Approach 3;
        """
        
        n = len(s)
        if n <= 1: return n
        
        n_res = 1
        pl, pr = 0, 1
        d = {s[0]:0}
        while pr < n:
            if s[pr] not in d:
                d[s[pr]] = pr
                pr += 1
            else:
                # This is "SyntaxError: invalid syntax": n_res = pr - pl if pr - pl > n_res
                if pr - pl > n_res: n_res = pr - pl 
                pl_tmp = d[s[pr]] + 1
                for i in range(pl, d[s[pr]]+1): d.pop(s[i])
                d[s[pr]] = pr  # don't forget this!
                pl = pl_tmp
                pr += 1
        
        # don't forget to compare the last.
        if pr - pl > n_res: n_res = pr - pl
        return n_res




# Algo. 3
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        : type s: str
        : rtype: int
        :
        : TC: Time Limit Exceeded with 986/987 test cases passed, O(n^3), see Approach 1 analysis.
        : SC: O(min(n, m)), see Approach 1 analysis.
        :\BF Algo. as Approach 1, 2 for-loop to check all possible substrings to see if they are unique, with
        : set. This algo. has a lot of redundant and unnecessary check and comparison, need to improve the TC.
        """
        
        n = len(s)
        if n <= 1: return n
        n_res = 1
        
        def allUnique(s, start, end):
            set_rec = set()
            for i in range(start, end):
                if s[i] in set_rec: return False
                else: set_rec.add(s[i])
            return True
        
        for i in range(n):
            for j in range(i+1, n+1):
                # be aware j is exclusive!
                if allUnique(s, i, j) and j-i > n_res: n_res = j - i
        
        return n_res

