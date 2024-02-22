# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        #[include,exclude]
        def dp(node):
            if node in memo:return memo[node]
            if not node:
                return [0,0]
            leftside = dp(node.left)
            rightside = dp(node.right)
            include = node.val+(leftside[1]+rightside[1])
            exclude = max(leftside)+max(rightside)
            memo[node] = [include,exclude]
            return memo[node]
        return max(dp(root))
        
        