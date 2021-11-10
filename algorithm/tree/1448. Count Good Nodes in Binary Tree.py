'''
run pre-order traversal
check every node that is the largest one.
and swap the previously max value if self is
the largest.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        
        def recursive(root, preval_max):
            nonlocal count
            
            if root is None:
                return
            
            if (val :=root.val) >= preval_max:
                count += 1
                preval_max = val

            recursive(root.left, preval_max)
            recursive(root.right, preval_max)
            
        recursive(root, float('-inf'))
        
        return count