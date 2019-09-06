# Algo. 1
class Solution:
    def intToRoman(self, num: int) -> str:
        """
        : Input num (int):
        : Output (str):
        :
        : TC: 86.35%, O(1), since n <= 4; 
        : SC: 6.15% (shoud be wrong), O(1); 
        :\Algo. 1 BF from Ligang, use a list of dictionary to represent all cases from 1-9, for 0 you do not need 
        : a value, also use str(num) to get the string representation of the integer value. 
        """       
        lst_map = [{"1":"I", "2":"II", "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX"}  \
                ,  {"1":"X", "2":"XX", "3":"XXX", "4":"XL", "5":"L", "6":"LX", "7":"LXX", "8":"LXXX", "9":"XC"}  \
                ,  {"1":"C", "2":"CC", "3":"CCC", "4":"CD", "5":"D", "6":"DC", "7":"DCC", "8":"DCCC", "9":"CM"}  \
                ,  {"1":"M", "2":"MM", "3":"MMM"}]
        
        str_res = ""
        str_n = str(num)
        n     = len(str_n)
        for i in range(n-1, -1, -1):
            if str_n[i] in lst_map[n-1-i]:
                # Be aware, i -> n-1-i; and not str_res += lst_map[n-1-i][str_n[i]] which would be wrong!
                str_res = lst_map[n-1-i][str_n[i]] + str_res
        
        return str_res


