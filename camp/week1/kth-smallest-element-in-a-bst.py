# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = self.inorder(root)
        number = arr[k-1]
        return number



    def inorder(self,root):
        if not root:return[]
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        return left + [root.val] + right