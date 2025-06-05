# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(node, is_left):
            if not node:
                return []
            if is_left and not node.left and not node.right:
                res.append(node.val)
            dfs(node.left, True)
            dfs(node.right, False)
        dfs(root, False)
        print(res)
        return sum(res)
