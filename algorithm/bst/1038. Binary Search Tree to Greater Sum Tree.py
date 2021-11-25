'''
First naive thought, using inorder loop out values O(n)
calculate the sum that needed O(n^2)
inorder traversal changes the value of the tree O(n)

which is pretty dump. (I have a feeling that this can by solved by one pass)
And yes, the second solution does it.
'''

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        val_list = inorder(root)
        sum_list = [sum(val_list[i:]) for i in range(len(val_list))]

        
        def add_inorder(node):
            if not node:
                return
            nonlocal sum_list

            add_inorder(node.left)
            node.val = sum_list[0]
            del sum_list[0]

            add_inorder(node.right)
            
            
        add_inorder(root)
        return root


'''
One pass right traversal solution
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        val = 0
        
        def right_inorder(node):
            
            nonlocal val            
            if not node: return None
            
            right_inorder(node.right)
            node.val = val = node.val+val
            right_inorder(node.left)
            
        right_inorder(root)
        return root
