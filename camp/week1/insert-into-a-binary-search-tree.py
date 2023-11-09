# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        def insert(parent,child):
            if child == None:
                if val > parent.val:
                    parent.right = TreeNode(val)
                else:
                    parent.left = TreeNode(val)
                return
            if val > parent.val:
                insert(child,parent.right)
            else:
                insert(child,parent.left)
        insert(root,root)
        return root 
        