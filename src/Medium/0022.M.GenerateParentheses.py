# Algo. 1
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        : type n: int
        : rtype: List[str]
        : 
        : TC: ?
        : SC: ?
        :\Algo. 1 BF with Recursion, compile error of "name 'generateParenthesis' is not defined". Need to check later.
        """
        if n <= 0: return []
        if n == 1: return ["()"]
        if n == 2: return ["()()", "(())"]
        
        lst_n1 = generateParenthesis(n-1)
        lst_res = []
        set_res = set()
        n_lst_n1 = len(lst_n1)
        for i in range(n_lst_n1):
            str_n1 = lst_n1[i]
            for j in range(2*(n-1)+1):
                str_n_1st = str_n1[0:j] + "(" + str_n1[j:]
                for k in range(j+1, 2*(n-1)+2):
                    str_n_2nd = str_n_1st[0:j] + ")" + str_n_1st[j:]
                    
                    set_res.add(str_n_2nd)
        
        return list(set_res)




# Algo. 1
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        : type n: int
        : rtype: List[str]
        : 
        : TC: O(f(n)*n^2), 9.81%, f(n) being the # of strings gerenated for n, n^2 accounts the 2 for-loop (with iteration integer j, k)
        : SC: f(n) for lst_n1; 5.08%, What about the stack for recursion? 
        :\Still Algo. 1 BF with Recursion, removed the previous compile error by defining a helper recursive function.
        : The problem is idealy for recursion, if you have result for n-1, how do you add a new pair of parenthesis 
        : to make it valid? First put "(" anywhere possible, then put ")" afterward anywhere possible. The problem is
        : it will generate duplicate result strings, so we use set to remove those duplicates. 
        """
        def helper(m):
            if m <= 0: return []
            if m == 1: return ["()"]
            if m == 2: return ["()()", "(())"]
            
            # yes we can do recursive call like this!
            lst_n1 = helper(m-1)
            set_res = set()
            n_lst_n1 = len(lst_n1)
            for i in range(n_lst_n1):
                str_n1 = lst_n1[i]
                for j in range(2*(m-1)+1):
                    str_n_1st = str_n1[0:j] + "(" + str_n1[j:]
                    for k in range(j+1, 2*(m-1)+2):
                        str_n_2nd = str_n_1st[0:j+1] + ")" + str_n_1st[j+1:]
                        
                        set_res.add(str_n_2nd)
            return list(set_res)
        
        return helper(n)


