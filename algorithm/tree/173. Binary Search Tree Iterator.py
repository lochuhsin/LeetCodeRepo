"""
Traversal all tree by inorder (get all values) and store in list
Then ..... simple, but i think this is does not achieve the problems
point. (To traverse bst inorder and stop at that point. Not traverse
all the possible node at first.)
"""
'''
BTW : after looking at the solution, the first solution appears to be
as same as mine LOL. (Flatten binary tree)
'''
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        def inorder(node):
            if not node:
                return None
        
            inorder(node.left)
            self.val_list.append(node.val)
            inorder(node.right)

        self.val_list = []
        self.index = 0    
        inorder(root)
   
    def next(self) -> int:
        val = self.val_list[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        return self.index < len(self.val_list)

"""
This is the real deal (control recursion) well... not really
stopping a recursion. However this solution is very clever,
The reason is the average maximum size of stack is O(h) the height of the tree.
(of course the worst case is O(n) if the bst is linear tree 5->4->3->2->1)
The above solution always uses O(n).
"""

class BSTIterator:

    def __init__(self, root: TreeNode):

        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):

        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """

        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # Need to maintain the invariant. If the node has a right child, call the
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0