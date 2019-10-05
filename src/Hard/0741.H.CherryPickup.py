# Algo. 1
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        :TC: NA, not finished; worth finish it up!
        :SC: NA
        :
        :\1st idea, traceback with recursion to try all cases? Should not be greedy? DP? Graph BFS or DFS?
        : 1st attempt, not finished.
        : Multiple paths to find out the maximum. 
        """
        def recur_func(grid, i, j, n_cherry):
            n = len(grid)
            if grid[i][j] == 1: n_cherry += 1
            
            if i == n-1 and j == n-1: 
                return n_cherry          
            elif i == n-1 and j != n-1:
                if grid[i][j+1] == -1: 
                    return 0
                else:
                    recur_func(grid, i, j+1, n_cherry)
            elif j == n-1 and i != n-1:
                if grid[i+1][j] == -1:
                    return 0
                else:
                    recur_func(grid, i+1, j, n_cherry)
            elif grid[i+1][j] == -1 and grid[i][j+1] == -1: 
                return 0
            else: 
                if grid[i+1][j] != -1:
                    recur_func(grid, i+1, j, n_cherry)
                if grid[i][j+1] != -1:
                    recur_func(grid, i, j+1, n_cherry)




