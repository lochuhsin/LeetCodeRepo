# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nodes = []
        
        def in_order_traverse(root):
            if root is None:return
            in_order_traverse(root.left)
            nodes.append(root)
            in_order_traverse(root.right)
        
        def build_balanced_tree(left, right):
            if left>right:return None
            mid = (left+right)//2
            root = nodes[mid]
            root.left = build_balanced_tree(left, mid-1)
            root.right = build_balanced_tree(mid+1, right)
            return root
        in_order_traverse(root)
        return build_balanced_tree(0, len(nodes)-1)
            
            
            