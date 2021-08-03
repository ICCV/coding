class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(treenode):
            while treenode.left != None:
                dfs(treenode.left)
            res.append(treenode.val)
            while treenode.right != None:
                dfs(treenode.right)
        return res