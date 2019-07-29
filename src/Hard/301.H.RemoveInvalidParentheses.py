# Algo. 1, 23/126 test cases passed, need to fix an obvious bug later.
# THIS ALGO. from Ligang IS WRONG! Check the 44/126 test case of "()())())))())(()",
# my output is ["(())()()()","()()()()()"], while the expected result is:
# ["((())())()","((()))()()","(()()())()","(()())()()","(())(())()","(())()()()","()(()())()","()(())()()","()()(())()","()()()()()"]
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        : type s: str
        : rtype: List[str]
        : 
        :\TC: ?, 23/126 test cases passed, with one obvious error to be fixed, which is to keep other characters. 
        :     keep it for record.
        : SC: ? will check later.
        :\Algo. 1 from Ligang, IT IS WRONG! the KEY idea is like Divide and conquer, when you check the string forward, 
        : whenever it has more ")" than "(" (actually it has one more of ")" than "("), then the passed substring 
        : can be processed independently (NO, YOU CAN NOT PROCESS IT INDEPENDENTLY! THERE ARE OTHER POSSIBILITIES), :        
        : the same procedure applies when you check the string backward, which in code implement, following the above 
        : forward checking, you have one last substring left which you have "(" more than or equal to ")", 
        : it's just from the point of understanding, you can look at this substring backward. 
        :\A lot of python language tips and tricks to be aware of.
        """
        # pre-process s
        lst_s = list(s)
        # list comprehension to remove certain items
        #\Tip: it's always a good idea to remove these NOISE first if allowed, or you'll have to
        # deal with it later, sometimes more difficult and tricky.
        # However it is WRONG to remove other characters! will fix it later.
        lst_s = [x for x in lst_s if x in {"(", ")"}]
        # use while-loop to remove starting ")", then it'll start with "("
        while lst_s and lst_s[0] == ")": lst_s.pop(0)  
        
        n = len(lst_s)
        if n <= 1: return [""]
        
        lst_res = []
        
        lst_stack = []
        for i in range(n):
            if lst_s[i] == "(": lst_stack.append(lst_s[i])
            else: lst_stack.append(lst_s[i])
            
            # Divide and conquer, anytime it happens, we can handle it and then get rid of it.
            # here lst_stack.count(")") = lst_stack.count("(") + 1, so you only need to remove 1 ")",
            # and no need to pop the last the ")" here.
            # print(lst_stack)
            if lst_stack.count(")") > lst_stack.count("("):
                print(lst_stack)
                if lst_stack[0] == ")": lst_stack.clear(); continue
                
                lst_idx    = []  
                for j in range(1, len(lst_stack)-1):
                    if lst_stack[j] == ")" and lst_stack[j+1] != ")":
                        lst_idx.append(j)
                        
                lst_substr = []
                # print("len(lst_idx) = " + str(len(lst_idx)))
                for j in range(len(lst_idx)): 
                    # WRONG!! then lst_tmp is a ref of lst_stack, and both point to a same list
                    # need to use list.copy() or [:] for a shallow copy!
                    # lst_tmp = lst_stack  
                    lst_tmp = lst_stack.copy()
                    lst_tmp.pop(lst_idx[j])
                    # lst_substr.append(lst_stack.pop(lst_idx[j]))
                    lst_substr.append(lst_tmp)
                    print("j = " + str(j) + ", lst_substr = ")
                    print(lst_substr)
                    
                # last case which should end with "))", it IS EASY to forget!!
                # lst_tmp = lst_stack
                lst_tmp = lst_stack[:]
                lst_tmp.pop(len(lst_tmp)-1)
                lst_substr.append(lst_tmp)
                print("lst_substr = ")
                print(lst_substr)

                
                if not lst_res: lst_res = lst_substr
                else: 
                    lst_res_tmp = lst_res
                    lst_res.clear()
                    for j in range(len(lst_res_tmp)):
                        for k in range(len(lst_substr)):
                            lst_res.append(lst_res[j] + lst_substr[k])
                
                print("lst_res = ")
                print(lst_res)
                lst_stack.clear()
        
        
        # last substring case where number of "(" >= number of ")"
        # Like this case "((()(()((", 
        while lst_stack and lst_stack[len(lst_stack)-1] == "(": lst_stack.pop(len(lst_stack)-1)
        if len(lst_stack) <= 1: lst_stack.clear()
        m = len(lst_stack)  # >= 2
        # now lst_stack start with "(" and end with ")"
        
        lst_substr   = []
        lst_stack_bw = []  # backward
        lst_res_bw   = []
        
        if lst_stack.count("(") == lst_stack.count(")"): 
            # print("if lst_stack.count("(") == lst_stack.count(")"):")  # invalid syntax
            print("if lst_stack.count('(') == lst_stack.count(')'):")  # NO error of invalid syntax.
            print(lst_stack) 
            lst_substr = lst_stack
            lst_res_bw = [lst_stack]  # here [] is NECESSARY!! or it'll be WRONG!!
        else:  # number of "(" > number of ")"
            for i in range(m-1, -1, -1):
                lst_stack_bw.append(lst_stack[i])
                # lst_stack_bw.insert(0, lst_stack[i])
                
                # lst_stack_bw.count("(") = lst_stack_bw.count(")") + 1
                # only need to remove one "("
                if lst_stack_bw.count("(") > lst_stack_bw.count(")"): 
                    if lst_stack_bw[0] == "(": lst_stack_bw.clear(); continue
                    
                    lst_idx = []
                    for j in range(1, len(lst_stack_bw)-1):
                        if lst_stack_bw[j] == "(" and lst_stack_bw[j+1] == ")":
                            lst_idx.append(j)
                    
                    # WRONG!! the string in the lst_stack_bw will be in the reverse order!
                    # need to reverse it!
                    lst_substr = []
                    for j in range(len(lst_idx)):
                        lst_tmp = lst_stack_bw
                        lst_tmp.pop(lst_idx[j])
                        lst_tmp.reverse()
                        lst_substr.append(lst_tmp)
                    # last case ending with "((", whichs IS EASY to forget!!
                    lst_tmp = lst_stack_bw
                    lst_tmp.pop(len(lst_tmp)-1)
                    lst_tmp.reverse()
                    lst_substr.append(lst_tmp)
                    
                    if not lst_res_bw: lst_res_bw = lst_substr
                    else:
                        lst_res_bw_tmp = lst_res_bw
                        lst_res_bw.clear()
                        for j in range(len(lst_substr)):
                            for k in range(len(lst_res_bw_tmp)):
                                lst_res_bw.append(lst_substr[j]+lst_res_bw[k])
                            
        # lst_res_tmp = lst_res
        # lst_res.clear()  
        
        lst_str_res = []
        print(lst_res)
        print(lst_res_bw)
        # str(lst_res[j]) = str(['(', '(', ')', ')']) = "'(', '(', ')', ')'" != "(())"  !
        
        if not lst_res_bw and not lst_res: return [""]
        
        if not lst_res_bw:
            for j in range(len(lst_res)):
                str_one = ""
                for k in range(len(lst_res[j])):
                    str_one += lst_res[j][k]
                lst_str_res.append(str_one)
            return lst_str_res
        
        if not lst_res:
            for j in range(len(lst_res_bw)):
                str_one = ""
                for k in range(len(lst_res_bw[j])):
                    str_one += lst_res_bw[j][k]
                lst_str_res.append(str_one)
            return lst_str_res
        
        # if lst_res and lst_res_bw:
        
        for j in range(len(lst_res)):
            str_one = ""
            for j2 in range(len(lst_res[j])):
                str_one += lst_res[j][j2]
            print("j = " + str(j) + ", str_one = " + str_one)
            for k in range(len(lst_res_bw)):
                str_two = ""
                for k2 in range(len(lst_res_bw[k])):
                    str_two += lst_res_bw[k][k2]
                print("k = " + str(k) + ", str_two = " + str_two)
                    
                lst_str_res.append(str_one + str_two)
        
        return lst_str_res




