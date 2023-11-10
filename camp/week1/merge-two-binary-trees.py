# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0
        if not root1 and not root2:
            return
        newNode = TreeNode(val1+val2)
        next1left = root1.left if root1 else None
        next2left = root2.left if root2 else None
        newNode.left = self.mergeTrees(next1left,next2left)
        next1right = root1.right if root1 else None
        next2right = root2.right if root2 else None
        newNode.right = self.mergeTrees(next1right,next2right)
        return newNode
        
        