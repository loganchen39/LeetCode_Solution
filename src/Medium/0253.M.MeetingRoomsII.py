# Algo. 1
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        : type intervals: List[List[int]]
        : rtype: int
        :
        : TC: O(n^2) for 2 for-loops for searching, O(nlogn) for intervals.sort(), 77/78 test cases pass, with "Time Limit Exceeded"
        : SC:O(n) for lst_sorted_ET (end_time), 
        :\Algo. 1, The key idea is to find the Maximum number of meetings which have overlap time!
        : First we need to sort all the meetings by start time, then for current meeting CM, the number of previous meetings 
        : which is overlapped with cm is those end_time > cm.start_time. need to sort the previous meetings
        : by their end_time as well, so you can compare to count the number of overlapped meetings, and then
        : all need to insert the current meeting's end_time (here sort and insert op. should be a key algo. for efficiency). The  
        : result is the maximum number of overlapped meetings. Check the code below for my previous wrong ideas about the solutions. 
        """
        n = len(intervals)
        if n <= 1: return n
        
        intervals.sort(key=lambda item: item[0])
      
        lst_sorted_ET = []
        lst_sorted_ET.append(intervals[0][1])
        
        n_res_max = 1
        n_curr    = 0
        for i in range(1, n):
            b_setted = False
            n_curr   = 0
            for j in range(0, i):
                if intervals[i][0] < lst_sorted_ET[j]: 
                    n_curr = i - j + 1
                    if n_curr > n_res_max: n_res_max = n_curr
                    b_setted = True
                        
                if intervals[i][1] < lst_sorted_ET[j]:
                    lst_sorted_ET.insert(j, intervals[i][1])
                    break
            else:
                lst_sorted_ET.append(intervals[i][1])
                # if not b_setted: n_curr = 1  # no need for this
        
        return n_res_max

    
        # idea is WRONG! Previously I thought the result of maximum number of meetings should be
        # consective, well, they do NOT have to be.
        #n_max_prev = 1
        #n_curr     = 1
        #end_time_prev = intervals[0][1]
        #for i in range(1, n):
        #    if intervals[i][0] < intervals[i-1][1]:
        #        n_curr += 1
                
            
        # idea is WRONG! it only finds the maximum number of meetings with a certain meetings, all of them may not 
        # overlap with each other, an extreme case is: [0, 15], [0, 1], [2,3], [3, 4], [5, 6], [7, 8], [8, 9],
        # Except the first meeting, the rest are all not overlapped.
        #n_join = [0 for _ in range(n)]
        #n_res = 0
        #for i in range(n):
        #    for j in range(i+1, n):
        #        if intervals[j][0] < intervals[i][1]: 
        #            n_join[i] += 1
        #            n_join[j] += 1
        #        else: break
        #return max(n_join)+1




# Algo. 2
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        : type intervals: List[List[int]]
        : rtype: int
        :
        :\TC: O(nlogn) or O(n^2logn)? 5.05%, n for "for i in range(1, n)", logn for "while low <= high", 
        : the other n for moving elements to insert an element in a sorted array?
        :\SC: O(n) for lst_sorted_ET (end_time), 5.34%
        :\Algo. 2, The key idea is to find the Maximum number of meetings which have overlap time!
        : First we need to sort all the meetings by start time, then for current meeting CM, the number of previous meetings 
        : which is overlapped with CM is those end_time > cm.start_time. Need to sort the previous meetings
        : by their end_time as well, so you can compare to count the number of previous overlapped meetings, and then
        : it needs to insert the current meeting's end_time (here the insertion to keep the sorted previous meeting by end time
        : is a key algo. for efficiency, ). Previously we used a for-loop to check which has TC of O(n), here we use the
        : Binary Search and Binary Insertion Sort, to find the index to insert, which is "high + 1". The number of comparison
        : is O(logn) which is better than O(n). Should we count the move of elements for inserting an element in a sorted array as O(n)?
        """
        n = len(intervals)
        if n <= 1: return n
        
        intervals.sort(key=lambda item: item[0])
      
        lst_sorted_ET = []
        lst_sorted_ET.append(intervals[0][1])
        
        n_res_max = 1
        # n_curr    = 0
        for i in range(1, n):
            n_curr   = 0
            
            low, high = 0, i-1
            while low <= high:
                mid = int((low+high)/2)
                if intervals[i][0] < lst_sorted_ET[mid]: high = mid - 1
                else: low = mid + 1
            # if high <= 0: high = 0  # no need, even if high==-1
            # it's actually: n_curr = i - (high+1) (before index high+1, there are high+1 meetings) + 1(current meeting)
            n_curr = i - high  
            if n_curr > n_res_max: n_res_max = n_curr
            
            low, high = 0, i-1
            while low <= high:
                mid = int((low+high)/2)
                if intervals[i][1] < lst_sorted_ET[mid]: high = mid - 1
                else: low = mid + 1
            lst_sorted_ET.insert(high+1, intervals[i][1])
        
        return n_res_max


