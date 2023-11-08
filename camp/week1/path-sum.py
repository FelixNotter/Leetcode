# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node,cur):
            if (not node.left) and (not node.right):
                return cur+node.val == targetSum
            left = False
            right = False
            if node.left:
                left = dfs(node.left,cur+node.val)
            if node.right:
                right = dfs(node.right,cur+node.val)
            return  left or right
        return dfs(root,0)

    


        