# Algo. 1
class Solution:
    def numberToWords(self, num: int) -> str:
        """
        : type num: int
        : rtype: str
        : 
        : TC: O(1), 99.30%
        : SC: O(1), 5.33%, NOT correct!?;
        :\For this kind of problem, normally the idea is to use while LOOP from right (Least Significant Digits, LSB;
        : Low-Order Bit; Right-Most Bit) to left (Most Significant Bit, MSB). If you are doing it from left to
        : right, then there are too many cases to deal with and it should be too complicated to implement.
        :\Be aware that 2^31=2,147,483,648, i.e. the maximum of num is about 2 billion. Since num is sperated by
        : Thousand, Million, Billion, so we can LOOP the num 3-digit by 3-digit. Each 3-digit conversion can be further 
        : divided to 2 subproblems: Convert 1-digit for "Hundred", and the last 2-digit integer. The idea
        : of my implementation is the same as Approach 1; 
        """
        
        # special case
        if num == 0: return "Zero"
        
        # spelled wrong: Twelve, Fourteen, Nineteen, Forty, Ninety
        d_1to19 = {0:"", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight"  \
                ,  9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen" \
                , 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
        d_2ndDigit = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}
        str_3d_unit = ["", "Thousand", "Million", "Billion"]  # Better not to put " " here around like "Thousand".
        
        str_res = ''
        str_tmp = ''
        
        # Loop over 3-digit by 3-digit
        i = 0
        rmdr = num%1000
        while rmdr >= 0:
            if rmdr == 0:  # rmdr can be 0, special case to deal first here. will be more comlicated to deal in the code below;
                i += 1
                if num == rmdr: break
                num = int((num - rmdr)/1000)
                rmdr = num%1000
                continue
            else:
                # To make it simple, get the 3 digits.
                i1 = rmdr%10
                i2 = int((rmdr-i1)/10)%10
                i3 = int(rmdr/100)  # or more precisely, i3 = int((rmdr-i1-i2*10)/100)
            
                i2d = rmdr%100
                if i2d <= 19: str_tmp = d_1to19[i2d]
                else: 
                    if i1 == 0: str_tmp = d_2ndDigit[i2]  # so you do NOT have extra " "
                    else: str_tmp = d_2ndDigit[i2] + " " + d_1to19[i1]
            
                if i3 > 0:
                    if str_tmp == "": str_tmp = d_1to19[i3] + " Hundred"  # so you do NOT have extra " "
                    else: str_tmp = d_1to19[i3] + " Hundred " + str_tmp
            
                str_tmp = str_tmp + " " + str_3d_unit[i] + " "
                str_res = str_tmp + str_res
            
                i += 1
                if num == rmdr: break
                num = int((num - rmdr)/1000)
                rmdr = num%1000
        
        return str_res.strip()




# Algo. 2 (as Approach 1 of Divide and conquer)
