# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def Valid(node, left, right):
            if not node:
                return True
            if not (left < node.val and node.val < right): 
                return False
            return Valid(node.left, left, node.val) and Valid(node.right, node.val, right)
        return Valid(root, float("-infinity"), float("infinity"))