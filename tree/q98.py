# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def bfs(node_list):
            if not node_list:
                return True
            tmp_node_list = []
            is_valid = True
            for node in node_list:
                if node.left:
                    if node.val <= node.left.val:
                        is_valid = False
                        break
                    else:
                        tmp_node_list.append(node.left)
                if node.right:
                    if node.val >= node.right.val:
                        is_valid = False
                        break
                    else:
                        tmp_node_list.append(node.right)
            if is_valid:
                return bfs(tmp_node_list)
            else:
                return False
        bfs([root])