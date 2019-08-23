# Algo. 1 failed, could NOT finish. 
class Solution:
    def decodeString(self, s: str) -> str:
        """
        : type s: str
        : rtype: str
        :
        : TC: NA,
        : SC: NA, 
        :\Algo. 1 from Ligang, could NOT finish! How to handle the case of s="ab3[cc3[dd3[e11[f3[g]h]i]]]jk" with 
        : multiple level?
        """
        n = len(s)
        if n == 0: return ""
        
        str_res = ""
        str_dgt = ""
        i = 0
        lst_stack = []
        while i < n:
            if "a" <= s[i] and s[i] <= "z": 
                str_res += s[i]
                i += 1
            elif "0" <= s[i] and s[i] <= "9":  # a unit starts
                str_dgt = s[i]
                i += 1
                while i < n:
                    if "0" <= s[i] and s[i] <= "9":
                        str_dgt += s[i]
                        i += 1
                    else:
                        break
                lst_stack.append(int(str_dgt))
                if s[i] != '[': print("ERROR: s[i] != '['"); return ""
                lst_stack.append('[') 
                i += 1
                
                while i < n:
                    if "a" <= s[i] and s[i] <= "z":
                        str_cha = s[i]
                        i += 1
                    elif "0" <= s[i] and s[i] <= "9":




# Algo. 2, not finished again;
class Solution:
    def decodeString(self, s: str) -> str:
        """
        : type s: str
        : rtype: str
        :
        : TC: NA,
        : SC: NA, 
        :\Algo. 1 from Ligang, could NOT finish! How to handle the case of s="ab3[cc3[dd3[e11[f3[g]h]i]]]jk" with 
        : multiple level?
        """
        # n = len(s)
        if not s: return ""
        
        str_res = ""
        # str_dgt = ""
        # i = 0
        lst_stack = [["", 1, ""]]
        str_alp, str_dgt = "", ""
        for c in s:
            if   c.isalpha(): str_alp += c
            elif c.isdigit(): str_dgt += c
            elif c == "[":
                lst_stack.append([str_alp, int(str_dgt), "["])
                str_alp, str_dgt = "", ""
            else:  # "]"
                str_tmp = lst_stack.pop()[0] + lst_stack.pop()[1]*str_alp

