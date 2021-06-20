## Recursion version

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSy(l,r):
            if (l == None) and (r == None):
                return True
            if (l == None) or (r == None):
                return False
            return (l.val == r.val) and isSy(l.left,r.right) and isSy(l.right,r.left)
        
        return isSy(root,root)