# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create 2 pointers
        fast, slow=head,head
        # make the fast pointer to jump nth node from end it should be deleted
        for i in range(n):
            fast=fast.next
        # when fast is past the last node
        if fast == None:
            return head.next
        # when fast is in between the nodes
        while fast.next!=None:
            slow=slow.next
            fast=fast.next
        slow.next = slow.next.next
        return head 