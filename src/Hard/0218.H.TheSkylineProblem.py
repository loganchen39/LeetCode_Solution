# Algo. 1
from heapq import *

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        : TC: 64.77%, O(n*logn) for sort? 
        : SC: 10%, O(n), for x_pos_sorted, hq_live, lst_res; 
        :
        :\1st idea, no idea at all! 
        :\Algo. 1 from Discuss "14 line python code, straightforward & easy to understand". For each
        : curr_x, it only needs the highest height that cover it, so use (min) heap (priority) queue 
        : to store this info. 
        """
        n = len(buildings)
        x_pos_sorted = sorted(set([b[0] for b in buildings] + [b[1] for b in buildings]))
        
        hq_live, lst_res = [], []
        idx, curr_hgt, prev_hgt = 0, 0, 0
        
        for curr_x in x_pos_sorted:
            # the latter has to be "<=". consider the 1st "2" in the example,
            # for any curr_x of left or right, it will "push"/include it's own rectangle. 
            while idx < n and buildings[idx][0] <= curr_x:   
                heappush(hq_live, (-buildings[idx][2], buildings[idx][1]))
                idx += 1
            
            # while hq_live:  # then "if hq_live[0][1] <= curr_x:", WRONG, ENDLESS loop!
            # Here the latter should be "<=", so if curr_x is Ri, then its own rectangle will be popped out,
            # Check the curr_x of 7, it will pop out the rectangle (3, 7, 15), leaving 2 rectangles of
            # [2, 9, 10], [5, 12, 12], because 12>=10, so it will have a point [7, 12]. 
            while hq_live and hq_live[0][1] <= curr_x:
                heappop(hq_live)
            
            # The highest height for covering curr_x, curr_x==12 => hq_live = [], curr_hgt = 0.
            curr_hgt = -hq_live[0][0] if hq_live else 0
            if curr_hgt != prev_hgt:  # whenever the highest height changes, append a new point.
                lst_res.append([curr_x, curr_hgt])
                prev_hgt = curr_hgt
        
        return lst_res




