# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def helper(node):
            if not node:
                return []
            return helper(node.left)+[node.val]+helper(node.right)
        res = helper(root)
        return res == sorted(set(res))
        
            



   