# Algo. 1
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        : type intervals: List[List[int]]
        : rtype: List[List[int]]
        :
        : TC: O(nlogn) for sort, the rest is O(n), 72.02%
        : SC: O(n) worst/O(1) best for lst_res, 5.08%, what about the SC for sort?
        :\First sort the intervals according the 1st element, then in a loop there are 2 cases, one is
        : no overlap, the other has overlap, might have several overlaps to concatenate, so in this 
        : situation we better use while loop, not for loop. 
        """
        
        def lst_rep(lst: List[int]) -> int:
            return lst[0]
        
        n = len(intervals)
        if n <= 1: return intervals
        
        intervals.sort(key=lst_rep)
        print(intervals)
        
        lst_res = []
        lst_tmp = []
        i = 0
        while i < n-1:
            if intervals[i][1] < intervals[i+1][0]: 
                lst_tmp = intervals[i]
                lst_res.append(lst_tmp)
                
                # be aware of the last element with no overlap, then it will not be looped due
                # to the end condition of "i < n-1"; we can not use end condition of "i < n"
                # as we are comparing i with i+1 element, or you'll have error of index out of range.
                if i==n-2:   
                    lst_res.append(intervals[i+1])
                i += 1
            else: 
                min_a = intervals[i][0]
                max_a = max(intervals[i][1], intervals[i+1][1])
                j = i+1  # this element is concatenated with overlap to previous "i" element.
                while j < n-1:
                    # be aware it's not "if intervals[j][1] >= intervals[j+1][0]: ", 
                    # intervals[j-1][1] can be larger than intervals[j][1], so we use max_a.
                    if max_a >= intervals[j+1][0]: 
                        max_a = max(max_a, intervals[j+1][1])
                        j += 1
                    else: 
                        break
                lst_tmp = [min_a, max_a]
                lst_res.append(lst_tmp)
                i = j+1  # since j is concatenated, we need to examine the j+1 element next.
                
                # same as above, need to check the last "independent" element
                if i==n-1: 
                    lst_res.append(intervals[i])
        
        return lst_res




# Algo. 2
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        : type intervals: List[List[int]]
        : rtype: List[List[int]]
        :
        : TC: O(nlogn) for sort, the rest is O(n), 44.79%
        : SC: O(n) worst/O(1) best for lst_res, 5.08%, what about the SC for sort?
        :\Algo 2 of sorting as in Approach 2, similar idea to Algo. 1, but this one is a lot simpler to implement!
        : Algo. 1 has seperate var of lst_tmp to store the temp result with several cases to handle, to compare afterwards, 
        : here we do NOT have seperate vars to store intermediate results, only with 2 simple cases (as we compare before-wards): 
        : if overlapped, update the current result interval; if not overlapped, add to the result list as a new element;
        """
        
        def lst_rep(lst: List[int]) -> int:
            return lst[0]
        
        n = len(intervals)
        if n <= 1: return intervals
        
        intervals.sort(key=lst_rep)
      
        lst_res, i = [intervals[0]], 1
        while i < n:
            if intervals[i][0] <= lst_res[len(lst_res)-1][1]:
                lst_res[len(lst_res)-1][1] = max(intervals[i][1], lst_res[len(lst_res)-1][1])
            else:
                lst_res.append(intervals[i])                
            i += 1
        
        return lst_res


