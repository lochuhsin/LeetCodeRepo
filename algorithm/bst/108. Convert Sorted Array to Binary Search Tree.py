'''
A little interesting problem, although the difficulty is easy, i still can't
figure out in the first place.

The target is building a height balanced tree with sorted input list.

As the input list are already sorted. Imagin that always cutting the array as half.
using the mid point as root.

for example:
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    1. first node.val = 5 -> left: [1, 2, 3, 4], right: [6, 7, 8, 9]
    2. second level left node.val = 3 -> left: [1, 2], right: [4]
    3. second level right node.val = 8 -> left: [6, 7], right: [9]

    repeat until finish
'''


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        nums = nums
        
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        
        return helper(0, len(nums) - 1)