# Algo. 1
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        : Input A (List[List[int]]): 
        : Input B (List[List[int]]):
        : Output (List[List[int]]):
        :
        : TC: 78.37%, O(min(m,n)) for while-loop;
        : SC: 6.06%, O(min(m,n)) for lst_res;
        :\Algo. 1 BF from Ligang with Two-pointers in a while-loop; 
        """
        if not A or not B: return []
        
        na, nb = len(A), len(B)
        ia, ib = 0, 0
        lst_res = []
        # print("na = " + str(na) + ", nb = " + str(nb))
        
        while ia < na and ib < nb:
            # print("ia = " + str(ia) + ", ib = " + str(ib))
            if   A[ia][1] < B[ib][0]: ia += 1
            elif B[ib][1] < A[ia][0]: ib += 1
            else:
                a = max(A[ia][0], B[ib][0])
                b = min(A[ia][1], B[ib][1])
                lst_res.append([a, b])
                
                if   A[ia][1] < B[ib][1]: ia += 1
                elif A[ia][1] > B[ib][1]: ib += 1
                else: 
                    ia += 1
                    ib += 1
        
        return lst_res


