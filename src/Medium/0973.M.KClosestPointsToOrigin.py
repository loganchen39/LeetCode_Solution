"""
\The key idea is to sort the array, and also keep the corresponding INDICES "sorted" which is
 what we really want. My first brute-force algo. is to use selection sort, whose TC is O(n^2), 
 it did not get accepted because of "Time Limit Exceeded", with 75/83 test cases passed. The 
 inefficient TC is an issue. Need improvement.
\Same algo. as above, but here I combine the distance and index together, which is a lot easier 
as you do NOT need to update a seperate index array, which is tricky. Again it did not get accepted 
because of "Time Limit Exceeded", with 75/83 test cases passed.

\Implemented "Approach 1: Sort". list.sort(key=myFunc, reverse=False) where myFunc is your own 
self-defined function one element of the list for comparison/sorting purpose. "Another difference 
is that the list.sort() method is only defined for lists. In contrast, the sorted() function accepts 
any iterable." Or you can use like "points.sort(key = lambda P: P[0]**2 + P[1]**2)". TC O(nlogn), 
SC O(n) for the Timsort algo. explained below. 
\Python uses an algorithm called Timsort: Timsort is a hybrid sorting algorithm, derived from merge 
sort and insertion sort, designed to perform well on many kinds of real-world data. It was invented 
by Tim Peters in 2002 for use in the Python programming language. The algorithm finds subsets of the 
data that are already ordered, and uses the subsets to sort the data more efficiently. This is done 
by merging an identified subset, called a run, with existing runs until certain criteria are fulfilled. 
Timsort has been Python's standard sorting algorithm since version 2.3. It is now also used to sort 
arrays in Java SE 7, and on the Android platform.

\Failed to implement "Approach 2: Divide and Conquer", submitted with runtime error, did NOT 
actually finish, will check later. 
\When we sort or swap, better be on the original "points" list, so eventually you can return 
points[:K]. Need to find the indices for swapping or sorting. 

\Implemented sucessfully the MinHeap (Priority Queue) algo. Below are the key points.
A. Use array to store MinHeap which is a binary complete tree. Let's use an array witn index starting 
from 1 and number of elements N, then the last non-leaf node is at [int(N/2)]; For each non-leaf 
node at [i], it's left-child and right-child are at [2*i] and [2*i+1]; This is a good 
ref: https://www.hackerearth.com/practice/notes/heaps-and-priority-queues/

A. The process of building MinHeap is bottom-top, you start from last non-leaf node, to the first 
root node, "for i in range(int(N/2), 0, -1): Adjust_MinHeap(sd_idx, i, N)"; 

A. When adjusting one certain non-leaf node at [idx], you check the smaller value and swap if 
necessary; One key here is that if the swapped-child is also non-leaf, then you need to use recursion 
to adjust the swapped-child again!; 

A. While extract_min, you first swap the first root node and last (leaf) node, and then adjust the 
first root node, be aware that the heap_size is reduced by 1; 

A. The Chinese Data Structue in C is a good ref. The TC should be O(n*logn), SC should be O(n); 
"""


def Adjust_MinHeap(sd_idx, idx, N):
    left  = 2*idx
    right = 2*idx + 1
    small = idx
    if left <= N and sd_idx[left][0] < sd_idx[small][0]:
        small = left
    if right <= N and sd_idx[right][0] < sd_idx[small][0]:
        small = right
        
    if small != idx:
        sd_idx[idx], sd_idx[small] = sd_idx[small], sd_idx[idx]
        Adjust_MinHeap(sd_idx, small, N)

def Build_MinHeap(sd_idx, N):
    for i in range(int(N/2), 0, -1):
        Adjust_MinHeap(sd_idx, i, N)
    
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        n = len(points)
        sd = [points[i][0]**2+points[i][1]**2  for i in range(n)]
        lst_res = []
        
        if K == 0:
            return []
        if K >= n:
            return points
        if K == 1:
            idx_min = sd.index(min(sd))
            return [points[idx_min]]  # has to have []!
        
        sd_idx = [[sd[i], i]  for i in range(n)]
        sd_idx.insert(0, [-1, -1])
        Build_MinHeap(sd_idx, n)
        heap_size = n
        for i in range(K):
            lst_res.append(points[sd_idx[1][1]])
            sd_idx[1], sd_idx[n] = sd_idx[heap_size], sd_idx[1]
            heap_size -= 1
            Adjust_MinHeap(sd_idx, 1, heap_size)
        
        return lst_res