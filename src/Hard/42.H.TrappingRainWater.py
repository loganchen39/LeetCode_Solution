# Algo. 1, BF.;
class Solution:
    def trap(self, height):
        """
        : type height: List[int]
        : rtype: int
        :
        : TC: 5.07%, O(n^2)
        : SC: 5.10%, should be O(1), why so bad? 
        :\BF algo., You can look or abstract the problem at different perspectives, which will lead you to different
        : solutions. Here the idea is simple, for each idx, where the amount of water can be trapped is determined by
        : the minimal of the highest height at both left and right sides, which is exactly the "Approach 1" in LC Solution; 
        : The TC should be O(n^2), where inside of each for-loop, you need to find the maximum at both left and right side,
        : thus the TC is not good! There should be room for improvement, by avoiding checking maximum at both side all the time;
        :\
        """
        
        n = len(height)
        if n <= 2: return 0
        
        n_res  = 0
        n_curr = 0
        for i in range(1, n-1):
            max_left  = max(height[0  :i])
            max_right = max(height[i+1:n])
            min_lr    = min(max_left, max_right)
            if height[i] < min_lr:
                n_res += min_lr - height[i]
            
        return n_res




# Algo. 2, DP; 
class Solution:
    def trap(self, height):
        """
        : type height: List[int]
        : rtype: int
        :
        : TC: 13.66%, O(n)
        : SC: 5.18%, O(n)
        :\DP algo. as in "Approach 2", Following the BF algo. as in "Approach 1", instead of computing the max_left and max_right for each idx repeatedly,
        : you can compute and store the max_left and max_right in one loop, thus the TC becomes O(n) which is a big improvement over 
        : the BF algo., 
        :\From LC comments, #2 is not DP actually, because the problem is not divided into 2 sub-problems, but 2 partial problems. 
        : It's just memoization. Although memoization is often used with DP, they're different concepts. Don't be misleading.
        """
        
        n = len(height)
        if n <= 2: return 0
        
        n_res  = 0
        n_curr = 0
        
        max_left  = [0]*n
        max_right = [0]*n
        max_left[0]    = 0
        max_right[n-1] = 0
        
        # initialize and then loop to compute the max_left
        max_left[1] = height[0]
        for i in range(2, n):
            # Make sure you are crystal clear about the meaning of each var like the max_left[i-1]
            if height[i-1] > max_left[i-1]: max_left[i] = height[i-1]
            else: max_left[i] = max_left[i-1]
            
        max_right[n-2] = height[n-1]
        for i in range(n-3, -1, -1):
            if height[i+1] > max_right[i+1]: max_right[i] = height[i+1]
            else: max_right[i] = max_right[i+1]
        
        for i in range(1, n-1):
            min_h = min(max_left[i], max_right[i])
            if min_h > height[i]: n_res += min_h - height[i]
            
        return n_res




#Algo 3, Two-point; 
class Solution:
    def trap(self, height):
        """
        : type height: List[int]
        : rtype: int
        :
        : TC: 24.36%, O(n)
        : SC: 5.18%, O(1), why still so bad? Because of the comments?
        :\Algo. Two-Point as in "Approach 4", the idea is, if max_right >= max_left, then for current index il (idx left), the water
        : at il is bounded by max_left, and you can accumulate the result which is certain to know, and vice versa for ir (idx right). 
        : Previously my problem at thinking the solution is some kind of one-way thinking, from left to right, for current
        : il (idx left), there are different scenarios as from the right side, the max_right might be bigger than than max_left,
        : or it might be smaller than max_left, so you can not decide the water amount at the index il. 
        """
        
        n = len(height)
        # Handle special cases first which is necessary!
        if n <= 2: return 0
        
        n_res  = 0
        
        max_left, max_right = height[0], height[n-1]
        il, ir = 1, n-2
        while il <= ir:  # should be <=, not <.
            if max_left <= max_right:
                if height[il] >= max_left: max_left = height[il]
                else: n_res += max_left - height[il]
                il += 1
            else:
                if height[ir] >= max_right: max_right = height[ir]
                else: n_res += max_right - height[ir]
                ir -= 1
            
        return n_res




# Algo. 4, Using Stack; 
class Solution:
    def trap(self, height):
        """
        : type height: List[int]
        : rtype: int
        :
        : TC: 10.38%, O(n);
        : SC: 5.18%, O(n) worst case for stack; 
        :\Algo. Stack as Approach 3, other solutions are like column-wise, where for each index of column, 
        : you'll know exactly the amount of water to store in this column, by computing the max_left and 
        : max_right, while this algo. is like row-wise, looping from left to right, for the current index
        : of column, you can NOT know the total amount of water to store in this column as you do NOT know
        : the max_right, but you can compute the row-wise water amount to store so far as 
        : height[i_curr] > height[lst_st[len(lst_st)-1]].
        : One Ref. at: https://leetcode.wang/leetCode-42-Trapping-Rain-Water.html 
        """
        
        n = len(height)
        # Handle special cases first which is necessary!
        if n <= 2: return 0
        
        n_res  = 0
        lst_st = []
        
        # you may not need this, try to generalize it. 
        # Find the 1st index to start storing water. 
        for i_start in range(n-1):
            if height[i_start] > height[i_start+1]: break
        if i_start >= n-2: return 0
        
        lst_st.append(i_start)
        i_curr = i_start+1
        while i_curr < n:
            # be careful it's height[lst_st[len(lst_st)-1]], not lst_st[len(lst_st)-1]!
            if height[i_curr] <= height[lst_st[len(lst_st)-1]]: 
                lst_st.append(i_curr)
                i_curr += 1
            else: 
                while lst_st and height[i_curr] > height[lst_st[len(lst_st)-1]]: 
                    # accumulate back the water to store, multi-row by multi-row.
                    i_poped = lst_st.pop()
                    if not lst_st: 
                        # then height[i_curr] is the highest bar from left-most to i_curr
                        # it'll all start from here again. This check is important, or you'll
                        # get ERROR of index out of range!
                        break
                    h_diff   = min(height[i_curr], height[lst_st[len(lst_st)-1]]) - height[i_poped]
                    dist = i_curr - lst_st[len(lst_st)-1] - 1
                    n_res += h_diff * dist
                
                lst_st.append(i_curr)
                i_curr += 1
                    
        return n_res




# Algo. 5, Using Stack;
class Solution:
    def trap(self, height):
        """
        : type height: List[int]
        : rtype: int
        :
        : TC: 13.66%, O(n);
        : SC: 5.18%, O(n) worst case for stack; 
        :\Algo. Stack as Approach 3, same as Algo. 4, with some code generalization, remove the code
        : to find the 'i_start'. 
        """
        
        n = len(height)
        # Handle special cases first which is necessary!
        if n <= 2: return 0
        
        n_res  = 0
        lst_st = []
        
        i_curr = 0
        while i_curr < n:
            if not lst_st: 
                lst_st.append(i_curr); 
                i_curr += 1
            else:
                if height[i_curr] <= height[lst_st[len(lst_st)-1]]:
                    lst_st.append(i_curr)
                    i_curr += 1          
                else:
                    while lst_st and height[i_curr] > height[lst_st[len(lst_st)-1]]:
                        i_poped = lst_st.pop()
                        if not lst_st: break
                        
                        h_diff = min(height[i_curr], height[lst_st[len(lst_st)-1]]) - height[i_poped]
                        dist   = i_curr - lst_st[len(lst_st)-1] - 1
                        n_res += h_diff * dist
                    lst_st.append(i_curr)
                    i_curr += 1
                    
        return n_res