# Algo. 1 Failed.
import copy
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        : TC: NA, failed; 30/36 test cases passed; 
        : SC: NA, failed; 30/36 test cases passed; 
        : 
        :\1st idea, backtrace and recursion to try all cases, to find the existing words; for DFS for graph; 
        :\Algo. 1 from Ligang using backtracking and recursion. One problem is that, for current one word, when  
        : backtracking, it has multiple paths, if you failed on one path, and have set those characters on the  
        : path to invalid "0", how do you recover them, for the next path to use?! The following case has exactly
        : this problem! For this problem, you can restore the letter after recursion, like what we did below. 
        : Then the following case worked!
        :\Failed test case at 29/36: [["a","b"],["a","a"]], ["aaba"], output: [], expected: ["aaba"], below is stdout:
        : i = 1, j = 1, wd = aba, bd_tmp = 
        : [['0', '0', '0', '0'], ['0', 'a', 'b', '0'], ['0', 'a', 'a', '0'], ['0', '0', '0', '0']]
        : i = 2, j = 1, wd = ba, bd_tmp = 
        : [['0', '0', '0', '0'], ['0', '0', 'b', '0'], ['0', 'a', 'a', '0'], ['0', '0', '0', '0']]
        : i = 1, j = 1, b_res = False
        : i = 2, j = 1, wd = aba, bd_tmp = 
        : [['0', '0', '0', '0'], ['0', '0', 'b', '0'], ['0', 'a', 'a', '0'], ['0', '0', '0', '0']]
        : i = 2, j = 2, wd = ba, bd_tmp = 
        : [['0', '0', '0', '0'], ['0', '0', 'b', '0'], ['0', '0', 'a', '0'], ['0', '0', '0', '0']]
        : i = 1, j = 2, wd = a, bd_tmp = 
        : [['0', '0', '0', '0'], ['0', '0', 'b', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0']]
        : i = 2, j = 1, b_res = False
        :
        :\The 2D array doesn't have to square, it failed at the 31st test case (30/36 test cases passed):
        : [["b"],["a"],["b"],["b"],["a"]], ["baa","abba","baab","aba"]
        """
        def recur_find(bd_tmp, wd, i, j) -> bool:
            if wd == "": return True
            # b_res    = False
            # print("i = " + str(i) + ", j = " + str(j) + ", wd = " + wd + ", bd_tmp = ")
            # print(bd_tmp)
            
            ltr = bd_tmp[i][j]
            
            if wd[0] == bd_tmp[i][j+1]:
                bd_tmp[i][j] = "0"
                b_res = recur_find(bd_tmp, wd[1:], i, j+1)
                if b_res: return True
            
            if wd[0] == bd_tmp[i][j-1]:
                bd_tmp[i][j] = "0"
                b_res = recur_find(bd_tmp, wd[1:], i, j-1)
                if b_res: return True
            
            if wd[0] == bd_tmp[i+1][j]:
                bd_tmp[i][j] = "0"
                b_res = recur_find(bd_tmp, wd[1:], i+1, j)
                if b_res: return True
                
            if wd[0] == bd_tmp[i-1][j]:
                bd_tmp[i][j] = "0"
                b_res = recur_find(bd_tmp, wd[1:], i-1, j)
                if b_res: return True
            
            if bd_tmp[i][j] == "0": 
                # if neither of above return True, restore the letter for later use, important!
                bd_tmp[i][j] = ltr  
                
            return False
            
        
        def isWordInBoard(bd_tmp, wd) -> bool:
            n_bd = len(bd_tmp)
            n_wd = len(wd)
            if n_wd == 0: return True
            
            for i in range(n_bd):
                for j in range(n_bd):
                    # find the first character, i, j can not be 0 or n_bd-1. 
                    if bd_tmp[i][j] == wd[0]:
                        # bd_tmp = bd.copy()
                        b_res = recur_find(bd_tmp, wd[1:], i, j)
                        # print("i = " + str(i) + ", j = " + str(j) + ", b_res = " + str(b_res))
                        if b_res: 
                            return True
            return False
        
        
        n_bd = len(board)
        n_wd = len(words)
        lst_res = []
        
        bd   = []
        # add invalid "0" around the boundary, to avoid boundary extra processing. 
        bd.append(["0"]*(n_bd+2))   
        for i in range(n_bd):
            bd.append(["0"] + board[i] + ["0"])
        bd.append(["0"]*(n_bd+2))
        
        for wd in words:
            # bd_tmp = bd.copy()  # not gonna work!
            bd_tmp = copy.deepcopy(bd)
            
            if isWordInBoard(bd_tmp, wd): 
                lst_res.append(wd)
                
        return lst_res




# Algo. 2
import copy
from collections import defaultdict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        : TC: 93.33%, worst case, O(n_row*n_col*4*L) ?
        : SC: 91.67, O(N) where N being the total number of letter in the dictionary, for trie.
        : 
        :\Algo. 2 from A.1 partially implemented by Ligang. Using dict to store trie, and backtracking to find the
        : matched words. One important issue is that you need to RESTORE the current character in the board, as 
        : commented in the code. 
        : 
        :\test case 30: 
        : [["a","b"],["c","d"]], ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
        : Output: ["ac","ab"], Expected: ["ab","ac","bd","ca","db"], found the problem, the fix is in the code.
        : trie = {
        :         'a': {'b': {'-': 'ab', 'b': {'-': 'abb'}}, 'd': {'-': 'ad', 'c': {'b': {'-': 'adcb'}}}, 'c': {'-': 'ac', 'b': {'-': 'acb'}}}, 
        :         'c': {'b': {'-': 'cb'}, 'a': {'-': 'ca'}}, 
        :         'b': {'d': {'-': 'bd'}, 'c': {'-': 'bc'}}, 
        :         'd': {'a': {'-': 'da', 'b': {'c': {'-': 'dabc'}}}, 'b': {'-': 'db'}}
        :        }
        """
        # create trie from words
        trie = {}
        for wd in words:
            t = trie
            for ch in wd:
                if ch not in t: t[ch] = {}
                t = t[ch]
            if "-" not in t:
                t["-"] = wd  # end of the word, consider the case, ["apple", "app"]
        
        #print(trie)
        
        n_row         = len(board   )
        n_col         = len(board[0])
        rc_offset     = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        matched_words = []
        
        
        def backtracking(r, c, dict_parent) -> None:
            ltr = board[r][c]
            board[r][c] = "$"
            
            if "-" in dict_parent: 
                matched_words.append(dict_parent["-"])
                # Can NOT return here! There may be other words, and the restore below is absolutely needed,
                # or the board in the above case in comment becomes: [['a', '$'], ['$', 'd']], which is wrong. 
                # return   
            
            for ro, co in rc_offset:
                # good practice of using loop to ease the coding.
                if r+ro < 0 or r+ro >= n_row or c+co < 0 or c+co >= n_col: continue
                if board[r+ro][c+co] in dict_parent: 
                    backtracking(r+ro, c+co, dict_parent[board[r+ro][c+co]])
            
            # restore
            board[r][c] = ltr
        
        
        for r in range(n_row):
            for c in range(n_col):
                #if r == 0 and c == 1: 
                #    print(board)
                if board[r][c] in trie:
                    backtracking(r, c, trie[board[r][c]])
        
        matched_words = list(set(matched_words))
        return matched_words




