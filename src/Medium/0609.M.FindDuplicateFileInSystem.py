# Algo. 1
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """
        :TC: 20.22%, O(n) n being number of files,
        :SC: 36.36%, O(n) n being number of files,
        :
        :\1st idea, use dict (HashTable), file content as key, it's duplicated file names (including path) as value;
        : loop over and check; This is Algo. 1 implemented by Ligang. Later check the follow-up questions.
        """
        n = len(paths)
        
        dict_fc_fns = defaultdict(list)
        for str_files in paths:
            lst_str = str_files.split()
            
            str_dir = lst_str[0]
            for i in range(1, len(lst_str)):
                fn, ch, fc = lst_str[i].partition("(")
                fc = fc[0:len(fc)-1]  # remove the last ")"
                dict_fc_fns[fc].append(str_dir + "/" + fn)
        
        lst_res = []
        for fc in dict_fc_fns:
            if len(dict_fc_fns[fc]) >= 2:
                lst_res.append(dict_fc_fns[fc])
        
        return lst_res


