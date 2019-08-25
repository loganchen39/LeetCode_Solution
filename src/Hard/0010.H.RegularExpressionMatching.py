# Algo. 0, not finished. 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        : type s: str
        : type p: str
        : rtype: bool
        :
        : TC:
        : SC:
        :\Algo. 0, initial idea, 2 pointers to s and p respectively, compare and move forward, s is fixed, 
        : p can be variable with "*" and ".". How to deal with several (unlimited) possibilities, with DP
        : or backtracking? 
        """
        ns, np = len(s), len(p)
        if ns == 0 and np == 0: return True
        if np == 0: return False  # ns == 0 and np != 0, it could be True
        
        # use a stack? 
        pt_s, pt_p = 0, 0
        while pt_s < ns:


