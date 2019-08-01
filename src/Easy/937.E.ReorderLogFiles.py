# Algo. 1 BF
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        : type logs: List[str]
        : rtype: List[str]
        : 
        : TC: 69.17%, O(n^2) worst, O(n) best; 
        : SC: 5.80%, O(n) for lst_letter and lst_digit; 
        :\Algo. 1 BF From Ligang, Loop-over and process each item, seperate letter and digit, 
        """
        n = len(logs)
        if n <= 1: return logs
        
        lst_letter = []
        lst_digit  = []
        # lst_res    = []
        for i in range(n):
            # here partition is a good function to use, not split.
            str_left, sep, str_right = logs[i].partition(" ")
            if str_right[0].isdigit(): lst_digit.append(logs[i])
            else:
                # need to initialize here, or if the len(lst_letter) = 0, it'll have the ERROR of 
                # "j not assigned."
                j = 0
                for j in range(len(lst_letter)):
                    str_l, sep_m, str_r = lst_letter[j].partition(" ")
                    # print("j = " + str(j) + ", str_right = " + str_right + ", str_r = " + str_r)
                    # for str you can compare like this!
                    if str_right <= str_r: 
                        break
                    # it's necessary, unlike C++, after the final loop step of j = len(lst_letter) - 1
                    # outside of loop, j will not become len(lst_letter), it's still len(lst_letter) - 1!
                    if j+1 == len(lst_letter): j += 1
                lst_letter.insert(j, logs[i])
        
        return lst_letter + lst_digit




# Algo. 2
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        : type logs: List[str]
        : rtype: List[str]
        : 
        : TC: 88.72%, O(nlogn) for sort;
        : SC: 5.80%, O(1) wrong? O(n)?; 
        :\Algo. 2 Custom sort as Approach 1. 
        """
        def f(log):
            # the self-defined key function used in python sort function can return numerical values,
            # strings, and like here tuples, etc, all of which can be "compared"!
            # the usage of this split function can substitute the string partition function. 
            id_, rest = log.split(" ", 1)
            
            # else digit value, keep the order, with the stable sort algo.
            return (0, rest, id_) if rest[0].isalpha() else (1, )   
        
        logs.sort(key=f)  # or return sorted(logs, key=f), extra space? 
        return logs

