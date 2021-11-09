# Thought process
'''
In order to find the least common ancestor (LCA)

loop every node in the tree, when root == p or root == q
return root (means we found the node)

Now ether left recursion or right recursion starts to return value
(since the node is found)

when in certain level of function stack that left return and right return
returns a value , this means the node in this level is the least common ancestor.

For one case need to consider. 
What if p is underneath q? ( or q is underneath p)

that indicates in certain node of left and right, one of them must be None.
Therefore after (if left and right) condition. adding return left or right.
Why return exactly ? because ether p or q is underneath each other. Therefore
The value themselves is the LCA
'''


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recursion(root, p, q):
            if root == p or root == q:
                return root

            
            left = right = None
            if root.left:
                left = recursion(root.left, p ,q)
                
            if root.right:
                right = recursion(root.right, p, q)
                
            if left and right:
                return root
            
            return left or right
        
        return recursion(root, p, q)