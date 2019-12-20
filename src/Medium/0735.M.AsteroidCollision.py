# Algo. 1
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        : TC: 49.42%, O(n), for the while-loop,
        : SC: 25%, O(n) for lst_stack,
        : 
        :\1st idea, two-pointers? stack? 
        :\Algo. 1 from Ligang using stack as A.1. These sort of problems that "LiangLiangDiXiao" are usually
        : good candidate for stack.
        """
        n = len(asteroids)
        lst_res = []
        
        ## the direction is not right!
        #for i in range(n):
        #    if asteroids[i] > 0: 
        #        idx_1stRight = i
        #        break
        #else:  # all moving right
        #    return asteroids
        
        #for i in range(n-1, -1, -1):
        #    if asteroids[i] < 0:
        #        idx_1stLeft = i
        #        break
        #else:  # all moving left
        #    return asteroids
        
        #if idx_1stRight > idx_1stLeft:  # left part moving left, and right part moving right, no intersection
        #    return asteroids
        
        if n <= 1: return asteroids
        
        lst_stack = []
        i = 0
        # for i in range(n-1):  # not good and flexible to use, sometimes you do NOT want to i+=1.
        while i < n:
            if lst_stack and lst_stack[-1] > 0 and asteroids[i] < 0: 
                if lst_stack[-1] > abs(asteroids[i]):
                    i += 1
                    continue
                elif lst_stack[-1] < abs(asteroids[i]):
                    lst_stack.pop() 
                else:  # ==
                    lst_stack.pop()
                    i += 1
            else:
                lst_stack.append(asteroids[i])
                i += 1
        
        return lst_stack




