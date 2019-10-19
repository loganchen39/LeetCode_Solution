# Algo. 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        # use member (or global) variable to keep track of the max_sum. 
        # Why it failed if I just "define" max_sum inside the function maxPathSum? It says the 
        # var is referred before it's been assigned. But I remember previously it worked, is it
        # because it's a recursion function (max_gain)? 
        self.max_sum = -float("inf")
        
        
    def maxPathSum(self, root: TreeNode) -> int:
        """
        :TC: 70.88%, O(n) n being total nodes, will visit every node at most twice.
        :SC: 5.55%, O(logN), need to keep a recursion stack of the size of the tree height, which is O(logN) for binary trees.
        :
        :\1st idea, loop or recursion to visit all cases, and record the maximum value?
        : For each current node, compute the max from left-tree and right, and record the maximum?
        :\Algo. 1 as A.1, implemented by Ligang Chen, my 1st idea makes sense. The key idea is, the path of 
        : max_sum for a node comes from (a path from) the left_tree through the node, and to (a path of) the
        : right_tree, and you check each node from this max_sum through recursion, which is quite common method
        : for binary tree. 
        """
        self.max_sum = -float("inf")
        
        def max_gain(node: TreeNode) -> int:
            if not node:  # Base case
                return 0
            
            left_gain  = max(max_gain(node.left ), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # check and reset.
            price_newpath = node.val + left_gain + right_gain
            if price_newpath > self.max_sum:
                self.max_sum = price_newpath
            
            # for current node, you still need to return its max_gain. 
            return node.val + max(left_gain, right_gain)
        
        
        max_gain(root)
        return self.max_sum


