# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        res=ListNode()
        res.next=head
        fast=slow=res
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow is fast:
                return True
        return False