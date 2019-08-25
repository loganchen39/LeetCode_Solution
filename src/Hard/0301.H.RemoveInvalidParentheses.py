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




# Algo. 2
class Solution:
    #def __init__(self, min_rem, cnt):  # no need here
        #self.min_rem = min_rem
        #self.cnt     = cnt
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        : type s: str
        : rtype: List[str]
        : 
        :\TC: O(2^n), 5.39%, in worst case, for each s[i], there are 2 cases to recurse, either adopt or discard; 
        : SC: O(n), 18.46%, 
        :\Algo. 2, as in Approach 1 Backtracking, like BF, with different implementation, need to check and  
        : implement LC A1 as well. Several tips below:
        :1. The idea is simply to check ALL POSSIBLE results by recursion, with certain cases no need to recurse and pass.
        :2. Whether the final expr is valid can be judged by "if left_count == right_count", this is because whenever
        :   we have right_count > left_count, we discard the current ")", as it'll make the final expr invalid for sure.
        :3. The correct recursion-call is like this: 
        :   helper(s, i+1, left_count+1, right_count, expr+s[i], rem_count, lst_res)
        :   it is like to compute the Fibonacci Numbers as: return fibonacci(n-1) + fibonacci(n-2);
        :   BE AWARE that you can not first set: i += 1; left_count += 1; expr += s[i]; then call-recursion like below:
        :   helper(s, i, left_count, right_count, expr, rem_count, lst_res)  # WRONG RESULTS!
        :4. For each recursion call like above, it will generate multiple threads; for certain thread which runs to the end, 
        :   the parameters passed with the recursive function, are like local vars. I NEED TO MAKE TESTS TO FIGURE OUT
        :   HOW RECURSION WORKS (WITH A STACK) CLEARLY!!
        :5. Previously I also passed the global minimun number of removals of min_rem, as a parameter to recursive function.
        :   it failed as in this case for each recursive thread, min_rem eventually is like a local var, it will always 
        :   become int(2**31-1) as initialized. you are not able to keep a global minimum for min_rem. One solution is
        :   to set min_rem as a class member so it will become a GLOBAL var, you can set and ref like self.min_rem = rem_count.
        :6. Why here lst_res works as a function parameter? Why it does not become like a local var? Should we also set
        :   it as a GLOBAL class member?
        :7. From LC A1: Such kind of problems where we have multiple options and we have no strategy or metric of deciding 
        :   greedily which option to take, we try out all of the options and see which ones lead to an answer. These type of 
        :   problems are perfect candidates for the programming paradigm, Recursion.
        """
        
        n = len(s)
        if not n: return [""]
        #if n == 1:
        #if n == 2:
            #if s != "()": return [""]
            # else: return ["()"]
            
        # compute global minimum
        
        lst_res = []
        i, left_count, right_count, rem_count = 0, 0, 0, 0  # local vars for each thread.  
        expr = ""
        # while i < n:  # iteration or recursion? 
        
        self.min_rem = int(2**31-1)  # GLOBAL class var member
        self.cnt = 0  # no need for this var, just like a test
        
        
        def helper(s, i, left_count, right_count, expr, rem_count, lst_res):
            n = len(s)
            if i < n:
                if s[i] != "(" and s[i] != ")":  # simple case, just include it.
                    #expr += s[i]  
                    #i += 1  # would be WRONG to set like this!
                    helper(s, i+1, left_count, right_count, expr+s[i], rem_count, lst_res)
                elif s[i] == "(":
                    # 1st case, adopt it
                    #left_count += 1
                    #expr += s[i]
                    #i += 1
                    helper(s, i+1, left_count+1, right_count, expr+s[i], rem_count, lst_res)
                    
                    # 2nd case, discard it
                    ##i += 1
                    #rem_count += 1
                    helper(s, i+1, left_count, right_count, expr, rem_count+1, lst_res)
                    
                    #i += 1
                else:  # s[i] == ")"
                    # with the current ")", right_count>left_count, would become invalid to include it for sure, so discard it.
                    if right_count >= left_count:  
                        # pass
                        #i += 1
                        #rem_count += 1
                        helper(s, i+1, left_count, right_count, expr, rem_count+1, lst_res)
                    else:  # left_count > right_count
                        # 1st case, adopt it
                        #right_count += 1
                        #expr += s[i]
                        #i += 1
                        helper(s, i+1, left_count, right_count+1, expr+s[i], rem_count, lst_res)
                        
                        # 2nd case, discard it
                        #rem_count += 1
                        ## i += 1
                        helper(s, i+1, left_count, right_count, expr, rem_count+1, lst_res)
                        
                        #i += 1
            else:  # i == n, final, check the result.
                self.cnt += 1
                # print("cnt = " + str(self.cnt) + ", min_rem = " + str(self.min_rem) + ", rem_count = " + str(rem_count) + ", expr = " + expr)
                
                if left_count == right_count:  # valid expr
                    if self.min_rem == int(2**31-1):
                        lst_res.append(expr)
                        self.min_rem = rem_count
                    elif rem_count < self.min_rem:
                        lst_res.clear()
                        lst_res.append(expr)
                        self.min_rem = rem_count
                    elif rem_count == self.min_rem:
                        lst_res.append(expr)
                    else:  # rem_count > min_rem, discard the result expr.
                        pass
                else:  # invalid expr
                    pass
            
        
        helper(s, i, left_count, right_count, expr, rem_count, lst_res)
        lst_res = list(set(lst_res))
        
        return lst_res




class Solution:     
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        : type s: str
        : rtype: List[str]
        : 
        :\TC: O(2^n) worst case, 52.19%, for each s[i], there are 2 cases to recurse, either include or discard; 
        : SC: O(n), 25.13%, 
        :\Algo. 3, as in Approach 2 Limited Backtracking, with different implementation, need to check and  
        : implement LC A2 as well. This algo. 3 follows Algo. 2 (as in A1) with some modifications. Several tips below:
        :1. We can calculate the number of opening/closing brackets to be removed, once the removal task finishes,
        :   you can stop (pass) the redundant (unnecessary) recusion process, only need to "copy" the rest substring.
        :2. Previously I thought left_rem and right_rem are global vars, which is WRONG! For each recursive thread,
        :   they are independent to use so they are local. If they are global, after the first thread, they both
        :   become 0, then for all of the rest threads, the algo. will not execute removal anymore, which is WRONG!
        :3. Other tips please check Algo. 2. 
        """
        
        n = len(s)
        if not n: return [""]
            
        # compute left_rem and right_rem
        left, right = 0, 0
        for i in range(n):
            if s[i] == "(": left += 1
            elif s[i] == ")": 
                if left > 0: left -= 1
                else: right +=1
        
        
        # local vars for each thread. 
        i, left_count, right_count, left_rem, right_rem, expr = 0, 0, 0, left, right, ""        
        self.lst_res = []  # this should be GLOBAL var, how come in Algo. 2, it's ok to be local?!
              
        
        def helper(s, i, left_count, right_count, left_rem, right_rem, expr):
            n = len(s)
            if i < n:
                if s[i] != "(" and s[i] != ")":  # simple case, just include it.
                    helper(s, i+1, left_count, right_count, left_rem, right_rem, expr+s[i])
                elif s[i] == "(":
                    # 1st case, include it
                    helper(s, i+1, left_count+1, right_count, left_rem, right_rem, expr+s[i])
                    
                    # 2nd case, discard it
                    if left_rem <= 0:
                        if right_rem == 0:
                            pass  # how to stop the recursion?! copy the rest substring? no need to stop?
                        else: 
                            pass
                    else:
                        # left_rem -= 1  # it would be WRONG if you set it like this.
                        helper(s, i+1, left_count, right_count, left_rem-1, right_rem, expr)
                    
                else:  # s[i] == ")"
                    # can only discard it, invalid expr, left_count and right_count are still needed!
                    if right_count >= left_count:  
                        if right_rem <= 0: 
                            print("ERROR: if self.right_rem <= 0:")
                        helper(s, i+1, left_count, right_count, left_rem, right_rem-1, expr)
                    else:    
                        # 1st case, include it
                        helper(s, i+1, left_count, right_count+1, left_rem, right_rem, expr+s[i])
                    
                        # 2nd case, discard it
                        if right_rem <= 0:
                            if left_rem == 0:
                                pass  # how to stop the recursion? copy the rest substring? 
                            else:
                                pass
                        else:
                            helper(s, i+1, left_count, right_count, left_rem, right_rem-1, expr)
            else:  # i == n
                if left_rem == 0 and right_rem == 0:
                    self.lst_res.append(expr)
                else:
                    print("ERROR: left_rem = " + str(left_rem) + ", right_rem = " + str(right_rem))
                    pass
            
        
        helper(s, i, left_count, right_count, left_rem, right_rem, expr)
        self.lst_res = list(set(self.lst_res))
        
        return self.lst_res


