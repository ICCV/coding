# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        tree_dict = {}#存储父节点
        tree_dict[root.val] = None
        def bfs(node_list):
            if not node_list:
                return
            tmp_list = []
            for node in node_list:
                if node.left:
                    tree_dict[node.left.val] = node
                    tmp_list.append(node.left)
                if node.right:
                    tree_dict[node.right.val] = node
                    tmp_list.append(node.right)
            bfs(tmp_list)
        bfs([root])
        res = []
        def dfs(node,from_node,d):
            if d == k:
                res.append(node.val)
                return
            for tmp_node in [node.left,node.right,tree_dict[node.val]]:
                if tmp_node == from_node or (not tmp_node):
                    continue
                d = d + 1
                dfs(tmp_node,node,d)
                d = d - 1
        dfs(target,target,0)
        return res
