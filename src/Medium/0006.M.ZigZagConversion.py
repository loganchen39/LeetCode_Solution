# Algo. 1
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        : TC: 51.65%, O(n), for while-loop (cnt: 0->n),
        : SC: 10%, O(n), for lst_str, 
        : 
        :\1st idea, loop and process, key point should be how the index changes. Make sure you understand
        : the rule of ZigZag. 
        :\Algo. 1 BF from Ligang using while-loop to process. 
        """
        n = len(s)
        # lst_str = [[]*numRows]  # WRONG!
        lst_str = [[] for i in range(numRows)]  # ok,
        
        cnt = 0
        while cnt < n:
            i = 0
            while i < numRows and cnt < n:  # do not forget we need this "cnt < n" here.
                lst_str[i].append(s[cnt])
                i   += 1
                cnt += 1
            
            i = numRows - 2
            while i > 0 and cnt < n:
                lst_str[i].append(s[cnt])
                ## Considering the result we want is a string without whilespaces, we actually do not need 
                ## these whilespaces " ". 
                #for j in range(numRows):
                #    if j != i: lst_str[j].append(" ")
                i   -= 1
                cnt += 1
        
        str_res = ""
        for i in range(numRows):
            str_tmp = "".join(lst_str[i])
            # the assignment is necessary! these functions like "replace" will not change the str_tmp directly,
            # it will just return the result string. REMEMBER str like tuple is not changable, that's why they 
            # can be key in a hash table (dictionary). Since we do not add these whitespaces above, here we also
            # do not need this.
            # str_tmp = str_tmp.replace(" ", "")
            str_res += str_tmp
        
        return str_res




