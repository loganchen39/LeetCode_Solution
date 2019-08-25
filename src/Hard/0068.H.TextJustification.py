# Algo. 1
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        : type words: List[str]
        : type maxWidth: int
        : rtype: List[str]
        :
        : TC: 80.98%, worst case O(n^2) where each word consists of one line, best case O(n) where all words consists of one line.
        : SC: 25%, O(n) for lst_res
        :\Algo. 1 BF from Ligang, idea is relatively simple as the problem is static, it's about looping and counting, and  
        : process differently according to different situations;
        """
        n = len(words)
        lst_res = []
        i = 0
        while i < n:
            j = i
            len_line = 0
            while j < n:  # loop to find the current line
                len_line += len(words[j])
                if j == n - 1:  # last word
                    break
                elif len_line + 1 + len(words[j+1]) > maxWidth:
                    break  # [i:j+1]
                else:
                    # for last word, no single space counted to len_line, other previous words each have one space counted
                    len_line += 1  
                    j += 1
            
            # found the line, process differently according to different situations;
            # nubmer of words: j-i+1, -1 because the last word has no space.
            # len_space is the total number of space, which needs to be distributed "evenly"
            len_space = maxWidth - len_line + (j-i+1-1)
            n_words   = j - i + 1
            if j == n - 1:  # last line, different process style for space
                str_tmp = ""
                for k in range(i, j):
                    str_tmp += words[k] + " "
                str_tmp += words[j]
                str_tmp += (len_space-(j-i))*" "
                lst_res.append(str_tmp)
                return lst_res
            
            if n_words == 1: 
                str_tmp = words[j] + len_space*" "
                lst_res.append(str_tmp)
            else:
                avg_space = int(len_space/(n_words-1))
                mod_space = len_space%(n_words-1)
                str_tmp = ""
                for k in range(i, j):
                    # just like in SODA_MPI how we distribute computational grid points to CPUs; 
                    str_tmp += words[k] + avg_space*" "
                    if k-i+1 <= mod_space: str_tmp += " "
                str_tmp += words[j]  # last word, total string length is exactly maxWidth.
                lst_res.append(str_tmp)
                
            i = j + 1
            if i > n - 1: break
        
        # return lst_res

