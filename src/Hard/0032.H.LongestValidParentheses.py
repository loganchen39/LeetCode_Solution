# Algo. 1
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        : TC: TLE, with 218/230 test cases passed. O(n^3)
        : SC: TLE, O(n) for substr and lst_stack, 
        :
        :\1st idea: match-up, counting, seems easy? "))(()(()" -> "(()(()" -> "((()" -> "((";
        : the above idea is WRONG for the case "()(()", 
        : Consider case: "()))CanBeSeperated((())(()(()", you never know what's in the end if it will make beforehand "(" valid!
        : Algo. 1 BF from A.1, check all non-empty even substrings if it's valid, return the maximum valid length.
        """
        def isValidParentheses(substr: str) -> bool:
            b_res     = True
            lst_stack = []
            for c in substr:
                if c == "(": 
                    lst_stack.append(c)
                else:
                    if not lst_stack: return False
                    else: lst_stack.pop()
            
            if lst_stack: return False
            else: return True
        
        
        n     = len(s)
        if n%2 == 0: m = n
        else: m = n-1
        for i in range(m, 0, -2):
            for j in range(0, n-i+1):
                if isValidParentheses(s[j:j+i]):
                    return i
        
        return 0




# Algo. 2
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        : TC: 71.90%. O(n),
        : SC: 44.44%, O(n), 
        :
        :\Algo. 2 as A.2 DP, Do NOT really understand yet! Need to check it out later!
        """
        maxans = 0
        n = len(s)
        dp = [0]*n
        
        for i in range(1, n):
            if s[i] == ")":
                if s[i-1] == "(":
                    if i >= 2: dp[i] = dp[i-2] + 2
                    else     : dp[i] = 0       + 2
                else:
                    if i-dp[i-1] > 0 and s[i-dp[i-1]-1] == "(":
                        if i - dp[i-1] >= 2:
                            dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                        else:
                            dp[i] = dp[i-1] + 0               + 2
                maxans = max(maxans, dp[i])
        
        return maxans


