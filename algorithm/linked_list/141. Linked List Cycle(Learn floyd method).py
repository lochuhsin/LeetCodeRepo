'''
it is easy to think of O(n) space complexity solution.
However O(1) is very genius.

This is floyd method. Two pointers with one fast, another slow.
If there is a loop in the linked list, the fast pointer will( and must)
eventually meet the slow pointer.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True