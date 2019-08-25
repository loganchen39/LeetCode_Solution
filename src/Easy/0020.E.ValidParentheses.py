# Algo. 1
class Solution:
    def isValid(self, s: str) -> bool:
        """
        : type s: str
        : rtype: bool
        :
        : TC: O(n), 98.68%
        : SC: 5.21%, O(1) normal, O(n) worst case with most characters are '(', '{', '['.
        :\Algo. 1 using stack perfectly for this kind of problem.
        """
        n = len(s)
        if not n: return True
        if n%2 == 1: return False

        # dict can be used like this for match. 
        d = {')': '(', '}':'{', ']':'['}
        lst_stack = []
        for i in range(n):
            if s[i] in {'(', '{', '['}: lst_stack.append(s[i])
            else:
                if not lst_stack or d[s[i]] != lst_stack[len(lst_stack)-1]: return False
                else: lst_stack.pop()
                    
        if lst_stack: return False
        else: return True

