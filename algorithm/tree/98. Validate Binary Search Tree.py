# my first thought of examine BST tree
'''
This is wrong, the reason is this solution only consider the 
previous node. That means: 

       10

    9      15

  1   13  3   12

This structure obviously is False, not a valid bst
but my algorithm returns true.
because in node 11 -> 1 and 13 are valid so node 11 returns True,
same as node 6 -> 3 and 7 are valid to 6, node 6 returns True.
But the position of 13, 3 is not valid to node 10. This is a huge
bug.
'''
class Solution: #wrong solution
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(node, preval, index):
            if not node:
                return True
            if index == 1 and node.val >= preval:
                return False
            
            elif index == 0 and node.val <= preval:
                return False

            left = check(node.left, node.val, 1)
            right = check(node.right, node.val, 0)
            
            #print(left, right)   
            return right and left
            
        
        return check(root, root.val, None)


"""
The correct one is using range
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))

        return validate(root)