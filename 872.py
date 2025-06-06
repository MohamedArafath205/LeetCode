# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, res):
            if not root:
                return res
            if root.left is None and root.right is None:
                res.append(root.val)

            dfs(root.left, res)
            dfs(root.right, res)
            return res

        left = dfs(root1, [])
        right = dfs(root2, [])
        print(left, right)
        return left == right
