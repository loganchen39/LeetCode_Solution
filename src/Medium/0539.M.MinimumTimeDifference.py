# Algo. 1
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        : TC: 80.02%, O(n*logn) for list sort, the rest is O(n),
        : SC: 100%, O(n) for lst_int_time,
        : 
        :\1st idea, loop over and compute the get the minimum, TC should be O(n**2), which is BF algo., 
        : will not implement here; or first convert to integer of hour/minute, then sort them, and then 
        : compute to get the minimum, may improve TC;
        :\Algo. 1 from Ligang with sorting, not the BF as mentioned above in 1st idea. 
        """
        n = len(timePoints)
        
        lst_int_time = []
        for str_time in timePoints:
            lst_tmp = str_time.split(":")
            # use minute as unit to store the time, referenced with 00:00, which is a good choice, as it
            # reduce the memory usage and ease the computation.
            lst_int_time.append(60*int(lst_tmp[0]) + int(lst_tmp[1]))
        
        lst_int_time.sort()
        int_res = float("inf")
        for i in range(n-1):
            time_diff = lst_int_time[i+1] - lst_int_time[i]
            if time_diff < int_res: int_res = time_diff
        # finally compare lst_int_time[n-1] and lst_int_time[0], do not forget this.
        if lst_int_time[0] + 24*60 - lst_int_time[n-1] < int_res: 
            int_res = lst_int_time[0] + 24*60 - lst_int_time[n-1]
        
        return int_res

    


