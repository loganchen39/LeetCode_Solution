# Alog. 1
class Solution:
    def calculate(self, s: str) -> int:
        """
        : Input, s (str): 
        : Output (int):
        :
        : TC: 40.11%, O(n) with for-loop,
        : SC: 11.11%, O(n) for lst_stack, 
        :\Algo. 1 from Ligang, Process each character in a for-loop, use a list/stack to store the intermediate 
        : results. Here we calculate the "*" and "/" first in the for-loop as they have higher priority than "+" and "-".
        : We may also process the string in a for-loop to the whole formula (not to calculate "*" and "/" first), 
        : and then compute the whole mathematical formula.
        """
        n = len(s)
        
        lst_stack = []
        str_curr_val = ""
        for c in s:
            if c.isdigit(): 
                str_curr_val += c
            else:
                if str_curr_val != "":
                    int_curr_val = int(str_curr_val)
                    m = len(lst_stack)
                    if m >= 2:
                        if lst_stack[m-1] == '*':
                            lst_stack[m-2] *= int_curr_val  # ok
                            lst_stack.pop()
                        elif lst_stack[m-1] == "/":
                            # lst_stack[m-2] /= int_curr_val  # it'll be float number
                            lst_stack[m-2] = int(lst_stack[m-2] / int_curr_val)
                            lst_stack.pop()
                        else:
                            lst_stack.append(int_curr_val)
                    else: 
                        lst_stack.append(int_curr_val)        
                    str_curr_val = ""
                    
                if c == " ":
                    continue
                else:
                    lst_stack.append(c)  # should be +,-,*,/
        else:  
            if str_curr_val != "":
                int_curr_val = int(str_curr_val)
                m = len(lst_stack)
                if m >= 2:
                    if lst_stack[m-1] == '*':
                        lst_stack[m-2] = lst_stack[m-2]*int_curr_val
                        lst_stack.pop()
                    elif lst_stack[m-1] == "/":
                        lst_stack[m-2] = int(lst_stack[m-2] / int_curr_val)
                        lst_stack.pop()
                    else:
                        lst_stack.append(int_curr_val)
                else:
                    lst_stack.append(int_curr_val)
                str_curr_val = ""
                    
        m = len(lst_stack)
        if m == 0: return None
        
        int_res = lst_stack[0]
        for i in range(2, m):
            # if lst_stack[i].isdigit():
            if lst_stack[i] not in {"+", "-"}:
                if lst_stack[i-1] == "+": 
                    int_res += lst_stack[i]
                elif lst_stack[i-1] == "-":
                    int_res -= lst_stack[i]
                else: 
                    print("ERROR: lst_stack[i-1] neither + nor -!")
        
        return int_res


