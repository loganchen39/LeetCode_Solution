# Algo. 1
class Solution:
    def __init__(self, b_res=False, set_sp=set()):
        self.b_res = b_res
        #self.idx_wd = idx_wd
        self.set_sp = set_sp
    

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        : type board: List[List[str]]
        : type word: str
        : rtype: bool
        :
        : TC: ? 85/87 test cases passed, with "Time Limit Exceeded", 
        : SC: ?
        :\Algo. 1 from Ligang, DFS with recursion. Step one is to find the 1st letter among the 2D board,
        : and then use DFS check and match the rest letters. Each found letter has four adjacent neighbours to 
        : check. You need a "set" (Hashtable) to store the searched path coords, so you can check to see if 
        : it's already visited for the current recursion, here the "set" self.set_sp is a GLOBAL class member, 
        : for each iteration of the 4 neighbours, make sure you RESET it to the original copy, or it might 
        : have visited all the cells when it move into the next iteration, and failed eventually! 
        :\The algo process is to try ALL possibilities, to find 1 True to make the result True, otherwise 
        : it's False. You can also set a GLOBAL class member variable self.b_res to store the result. 
        """
        if not board or not board[0]: return False
        nr, nc = len(board), len(board[0])
        nw = len(word)
        if nw == 0: return True
        
        # find the coords of the 1st letter
        lst_coords_1st_letter = []
        for i in range(nr):
            for j in range(nc):
                if board[i][j] == word[0]:
                    lst_coords_1st_letter.append((i, j))
        if len(lst_coords_1st_letter) == 0: return False
        if nw == 1: return True
        if nr*nc < nw: return False
        
        
        def dfs(bd, wd, curr_coord, idx_wd):
            nr, nc = len(board), len(board[0])
            nw = len(word)
            nbr = [(-1, 0), (0, -1), (0, 1), (1, 0)]
                    
            # print("Entering dfs, curr_corrd=" + str(curr_coord) + ", idx_wd = " + str(idx_wd) + ", wd[idx_wd] = " + wd[idx_wd])
             
            set_sp_bak = self.set_sp
            for k in range(4):
                # Have to RESET as it's global class member! if just assign as set_sp_bak, not work! just a ref!
                # While the LOCAL var idx_wd doesn't need to; 
                self.set_sp = set_sp_bak.copy()  
                i, j = curr_coord[0] + nbr[k][0], curr_coord[1] + nbr[k][1]
                if i >= 0 and i < nr and j >= 0 and j < nc and (i,j) not in self.set_sp and bd[i][j] == wd[idx_wd]:
                    if idx_wd == len(wd) - 1:  # returning condition
                        self.b_res = True
                        return
                    
                    self.set_sp.add((i, j))
                    # idx_wd += 1    
                    # if (i, j) == (1, 2):  # this comparison is ok
                    # print("In dsf, (i, j)=" + str((i, j)) + ", idx_wd = " + str(idx_wd))
                
                    # Normally you do NOT first set idx_wd += 1, and then call recursive dfs function with idx_wd!
                    dfs(bd, wd, (i, j), idx_wd+1)
            return
        
        
        self.b_res  = False
        self.set_sp = set()
        for i in range(len(lst_coords_1st_letter)):
            self.set_sp = {lst_coords_1st_letter[i]}
            idx_wd = 1 
            dfs(board, word, lst_coords_1st_letter[i], idx_wd)
            
            #print("i=" + str(i) + ", b_res=" + str(self.b_res) + ", idx_wd=" + str(idx_wd))
            #print(self.set_sp)
            if self.b_res: return True
            
        return False


##below is a good test case, to know the details of how recursion works,
##and its interaction with the GLOBAL/LOCAL variables. 
# [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
# "ABCESEEEFS"

# Entering dfs, curr_corrd=(0, 0), idx_wd = 1, wd[idx_wd] = B
# Entering dfs, curr_corrd=(0, 1), idx_wd = 2, wd[idx_wd] = C
# Entering dfs, curr_corrd=(0, 2), idx_wd = 3, wd[idx_wd] = E
# Entering dfs, curr_corrd=(0, 3), idx_wd = 4, wd[idx_wd] = S
# Entering dfs, curr_corrd=(1, 3), idx_wd = 5, wd[idx_wd] = E
# Entering dfs, curr_corrd=(1, 2), idx_wd = 6, wd[idx_wd] = E
# Entering dfs, curr_corrd=(2, 2), idx_wd = 7, wd[idx_wd] = E
# Entering dfs, curr_corrd=(2, 3), idx_wd = 8, wd[idx_wd] = F
# Entering dfs, curr_corrd=(2, 3), idx_wd = 6, wd[idx_wd] = E
# Entering dfs, curr_corrd=(2, 2), idx_wd = 7, wd[idx_wd] = E
# Entering dfs, curr_corrd=(1, 2), idx_wd = 8, wd[idx_wd] = F
# Entering dfs, curr_corrd=(1, 1), idx_wd = 9, wd[idx_wd] = S
# Entering dfs, curr_corrd=(1, 2), idx_wd = 4, wd[idx_wd] = S
# Entering dfs, curr_corrd=(1, 3), idx_wd = 5, wd[idx_wd] = E
# Entering dfs, curr_corrd=(0, 3), idx_wd = 6, wd[idx_wd] = E
# Entering dfs, curr_corrd=(2, 3), idx_wd = 6, wd[idx_wd] = E
# Entering dfs, curr_corrd=(2, 2), idx_wd = 7, wd[idx_wd] = E
# i=0, b_res=True, idx_wd=1
# {(0, 0)}
# 
# Entering dfs, curr_corrd=(2, 0), idx_wd = 1, wd[idx_wd] = B
# i=1, b_res=True, idx_wd=1
# {(2, 0)}

