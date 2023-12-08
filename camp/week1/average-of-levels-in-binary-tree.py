# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        res = []
        while queue:
            avg = 0
            n = len(queue)
            print(n)
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                avg+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg = avg/n
            res.append(avg)
        return res

