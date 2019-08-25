# Algo. 1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """
        : Encodes a tree to a single string.
        :
        : type root: TreeNode
        : rtype: str
        : TC: O(n), 7.49%
        : SC: O(n), 23.07%
        :\Algo. 1 DFS PreOrderTraverse (with recursion) as Approach 1, 
        : From LC: BFS; DFS: The DFS strategy can further be distinguished as preorder, inorder, 
        : and postorder depending on the relative order among the root node, left node and right node.
        : This serialization can be understood.
        : Recursion vs. Iteration + Stack (Queue).
        """
        if not root: return "None"
        lst_res = []
        self.str_res = ""
        
        # PreOrder/MidOrder/PostOrder are all not suitable for this problem? WRONG
        def DFS_PreOrder(p):
            if p: 
                self.str_res += str(p.val) + ","
                DFS_PreOrder(p.left)
                DFS_PreOrder(p.right)
            else:
                self.str_res += "None,"
        
        DFS_PreOrder(root)
        return self.str_res
            
       
    def deserialize(self, data):
        """
        : Decodes your encoded data to tree.
        :
        : type data: str
        : rtype: TreeNode
        : Algo. 1 as in Approach 1, recursion, not fully understand, need to re-visit!
        """    
        def r_helper(lst_str):
            if lst_str[0] == "None":
                lst_str.pop(0)
                return None
            
            root = TreeNode(int(lst_str[0]))
            lst_str.pop(0)
            root.left = r_helper(lst_str)
            root.right = r_helper(lst_str)
            return root
        
        
        # if not data or data.isspace(): return None
        # first string to list
        lst_str = data.split(",")
        lst_str.pop(len(lst_str)-1)  # remove the last ""
        if len(lst_str) <= 0: return None
        
        root = r_helper(lst_str)
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))




