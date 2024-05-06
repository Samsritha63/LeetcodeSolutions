# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node):
            if node.next is None:
                return node
            new_head = dfs(node.next)
            if node.val >= new_head.val:
                node.next = new_head
                return node
            return new_head
        return dfs(head)