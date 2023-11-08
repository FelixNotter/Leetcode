# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def symmetry(self,root1,root2):
        if not root1 and not root2:return True
        if (root1 is None) != (root2 is None):
            return False
        if root1.val != root2.val:
            return False
        return self.symmetry(root1.left,root2.right) and self.symmetry(root1.right,root2.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:return True
        return self.symmetry(root.left,root.right)

