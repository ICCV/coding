# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def bfs(node_list):
            if not node_list:
                return
            tmp_list = []
            for node in node_list:
                if node.left:
                    tmp_list.append(node.left)
                if node.right:
                    tmp_list.append(node.right)
                tmp_node = node.left
                node.left = node.right
                node.right = tmp_node
            bfs(tmp_list)
        bfs([root])
        return root

