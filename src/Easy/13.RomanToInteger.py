# Algo. 1.0
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        : Input  s (str): Description;
        : Output (int): Description;
        :
        : TC: 79.44%, O(n)
        : SC: 5.38% (May be wrong), O(1), for dictionary.
        :\Algo. 1 BF from Ligang, just need to classify different situations. Use HashTable (Dictionary and Set) for time efficiency  
        : and easy implementation; 
        """
        n = len(s)
        if n == 0: return 0
        
        dMap    = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        sMinus  = {"I", "X", "C"}
        sMinus2 = {"IV", "IX", "XL", "XC", "CD", "CM"}
        
        iRes = 0
        # Since for some cases it needs: i += 2, so while-loop here is more suitable than for-loop!
        # for i in range(n):
        i = 0
        while i <= n-1:
            if s[i] not in sMinus or i == n-1: 
                iRes += dMap[s[i]]
                i += 1
            else:
                if s[i:i+2] in sMinus2:
                    iRes += dMap[s[i:i+2]]
                    i += 2
                else:
                    iRes += dMap[s[i]]
                    i += 1
        
        return iRes


# Algo. 1.1, same as Algo. 1.0
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        dict_2 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        
        n_len = len(s)
        idx   = 0
        i_res = 0
        while idx<=n_len-2:
            if s[idx:idx+2] in dict_2.keys():
                i_res = i_res + dict_2[s[idx:idx+2]]
                idx += 2
            else:
                i_res = i_res + dict_1[s[idx]]
                idx += 1
        
        if idx==n_len-1:
            i_res = i_res + dict_1[s[idx]]
        
        return i_res

