class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        def right_tree(node, level):
            if not node:
                return 
            if level == len(res):
                res.append(node.val)
            right_tree(node.right, level+1)
            right_tree(node.left, level+1)
        right_tree(root, 0)
        return res
