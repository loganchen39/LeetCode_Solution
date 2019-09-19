# Algo. 1
import collections

class Solution:
    def calculate(self, s: str) -> int:
        """
        : TC: 7.12%, O(n), 
        : SC: 7.14%, O(n), 
        :
        :\First thought: loop over the string and process, priotirize with parentheses, most likely use stack.
        :\Original WRONG idea 1: since s only has + and -, the parentheses do not take effect and we can ignore them.
        : Consider case: "2-(5-6)", it's not all "+"!
        :\Original WRONG idea 2: Without any parentheses, the order of calculation does not matter, we can use
        : stack and calculate from the end. Consider case: "2-1+2", the calculation order from left to right matters!
        :\Originally I did not convert the string to the list stack, tried to loop and process directly on the string, 
        : the problem is there are several cases to think of, particularly regarding to ")" case, which made it 
        : complicated. Anyhow, will try to re-implement later.
        :\Algo. 1 BF from Ligang using stack. The conversion from string to list stack of integers and +/-/(/), and  
        : then process, made it a little, straightforward and easier. For regular cases without "(" and ")", you can 
        : simply process from left to right; For cases with ")", it could be (1-(2-3)), or (1-(2)), or (1)-(2), after  
        : remove (inside) parentheses, also need to calculate (1 - -1), (1 - 2) etc. 
        :\Test case 29/37: "(3-(5-(8)-(2+(9-(0-(8-(2))))-(4))-(4)))"
        """
        if not s: return 0
        
        int_res      = 0
        lst_stack    = collections.deque([])
        n_op         = 0
        str_curr_num = ""
        
        for v in s:
            if v.isdigit():
                str_curr_num += v
            elif v in {"+", "-", "(", ")"}:    # == "+" or v == "-":
                if str_curr_num != "":
                    lst_stack.append(int(str_curr_num))
                    str_curr_num = ""
                lst_stack.append(v)
            elif v == " ": 
                pass
        else:
            if str_curr_num != "":
                lst_stack.append(int(str_curr_num))
                lst_curr_num = ""
        
        
        n = len(lst_stack)
        # print(lst_stack)
        # lst = collections.deque([])
        lst = []
        for v in lst_stack:
            m = len(lst)
            if m >= 3 and type(lst[m-1]) == int and lst[m-2] in {"+", "-"} and type(lst[m-3]) == int:
                # Here this case mainly comes from "elif v == ')'" and cases like 1-(2), after removing
                # the parentheses, it becomes 1-2, need to calculate right after. 
                # Since it calculates from the end, make sure you do not have intermediate cases like:
                # 2-1+2. 
                if lst[m-2] == "+":
                    n_exp = lst[m-3] + lst[m-1]
                elif lst[m-2] == "-":
                    n_exp = lst[m-3] - lst[m-1]
                # TypeError: sequence index must be integer, not 'slice'. This operation is NOT for deque, but list.
                del lst[m-3:m]  
                lst.append(n_exp)
            
            lst.append(v)
            m = len(lst)
            if m >= 3 and type(lst[m-1]) == int and lst[m-2] in {"+", "-"} and type(lst[m-3]) == int:
                if lst[m-2] == "+":
                    n_exp = lst[m-3] + lst[m-1]
                elif lst[m-2] == "-":
                    n_exp = lst[m-3] - lst[m-1]
                # TypeError: sequence index must be integer, not 'slice'. This operation is NOT for deque, but list.
                del lst[m-3:m]  
                lst.append(n_exp)
            elif v == ")":
                if type(lst[m-2]) == int and lst[m-3] == "(":
                    n_exp = lst[m-2]
                    del lst[m-3:]
                    lst.append(n_exp)
                else:
                    if lst[m-3] not in {"+", "-"} and type(lst[m-2]) != int and type(lst[m-4]) != int and lst[m-5] != "(":
                        print("Should be ERROR: with v as )!")
                    if lst[m-3] == "+":
                        n_exp = lst[m-4] + lst[m-2]
                    elif lst[m-3] == "-":
                        n_exp = lst[m-4] - lst[m-2]
                    del lst[m-5:]
                    lst.append(n_exp)
        
        #print (lst)
        m = len(lst)
        int_res = lst[0]
        if m == 1: 
            return lst[0]
        else:
            for i in range(1, m, 2):
                if lst[i] == "+":
                    int_res += lst[i+1]
                elif lst[i] == "-":
                    int_res -= lst[i+1]
                else:
                    print("Should be ERROR: neither + or -!")
        return int_res


