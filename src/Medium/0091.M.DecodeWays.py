# Algo. 1.0
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        : Input  s (str): Description;
        : Ourput (int)  : Description;
        :
        :\TC: 86.64%, O(2^n), use extreme case (here like all "1"s) to get the worst TC, here the algo. is 
        : the same as the Fibonacci recursive function, you can use Dynamic Programming (or called Memoization)
        : to improve the efficency to O(n), see ref. CtCI p. 133.
        :\SC: 16%, same analysis as TC, worst case O(2^n) for extreme case (e.g. all "1"s), because of the 
        : 2 recursion stack. What if we use Dynamic Programming? see ref. CtCI p. 133.
        :
        :\Algo. 1 from Ligang, First by writing down and checking some simple cases, you will know that you 
        : NEED to split the whole string into several segments as follows, and then for each segment of length n, 
        : by checking some simple cases, there is some relationship between f(n) and f(n-1) etc. For example,
        : you have a SEGMENT of length 6 (i.e. "222222" from one type of segment), what if you add a new character
        : of "1" at the beginning, to form "1222222", you will figure out the relation: 
        : f(7) = f(6) (i.e. start with "1" ) + f(5) (i.e. start with "12"). The segments normally end with character
        : of "0", or "3"-"9", Below are different cases:
        :1. Example "112129", end with "3"-"9", the last second character is "2", last two characters like "28" not valid;
        :2. Example "112119", end with "3"-"9", the last second character is "1", last two characters like "18" valid;
        :3. Example "112120", end with "0", the last second character is "1" or "2", or the whole string is invalid, return 0;
        :   Originally I forgot this "0" case, and then wanted to remove all "0"s which is wrong! "10" is valid, while "01" 
        :   or "100" is invalid and need to return 0.
        :\Since you NEED to solve the problem Segment by Segment, you can use a List to store the Segment, after
        : processsing, clear the List and restart. if any Segment starts with "0", it's invalid and need to return 0
        : as the result. The final result is calculated by Rule of Product, or Multiplication Principle. 
        """
        def recur_func0(m: int) -> int:
            # case type: "112129", pay attention to the last two characters.
            # m >=2 or you still can set if m == 1: return 1;
            if m == 2: return 1
            if m == 3: return 2
            return recur_func0(m-1) + recur_func0(m-2)
        
        
        def recur_func1(m: int) -> int:
            # case type: "221213", pay attention to the last two characters.
            # m >= 2 or you still can set if m == 1: return 1;
            if m == 2: return 2
            if m == 3: return 3
            return recur_func1(m-1) + recur_func1(m-2)
        
        
        n = len(s)
        if n == 0: return 0
            
        i_res = 1
        lst_slice = []
        for c in s:
            if c == "0": 
                # pass
                m = len(lst_slice)
                if m == 0: return 0
                elif lst_slice[m-1] >= 3: return 0
                else:  # last two characters: "10" or "20"
                    del lst_slice[m-1:m]
                    m = len(lst_slice)
                    if m <= 1: 
                        # i_res = i_res * 1
                        lst_slice.clear()
                    else:
                        # Rule of product, or multiplication principle
                        i_res = i_res * recur_func1(m)  
                        lst_slice.clear()
            elif int(c) <= 2: 
                lst_slice.append(int(c))
            else:  # int(c) >= 3
                lst_slice.append(int(c))
                m = len(lst_slice)
                if m == 1:
                    # i_res = i_res*1
                    lst_slice.clear()
                elif lst_slice[m-2] == 2 and lst_slice[m-1] >= 7:
                    i_res = i_res * recur_func0(m)
                    lst_slice.clear()
                else:
                    i_res = i_res * recur_func1(m)
                    lst_slice.clear()
        else:  # do NOT forget this! The last Segment.
            m = len(lst_slice)
            if m == 0: return i_res
            
            if m == 1:
                # i_res = i_res*1
                lst_slice.clear()
            elif lst_slice[m-2] == 2 and lst_slice[m-1] >= 7:
                i_res = i_res * recur_func0(m)
                lst_slice.clear()
            else:
                i_res = i_res * recur_func1(m)
                lst_slice.clear()
        
        return i_res

