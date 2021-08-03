# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rv,res = root.val,-1
        def bfs(queue_list):
            if not queue_list:
                return
            tmp_list = []
            for q in queue_list:
                if q.val > rv:
                    if res == -1:
                        res = q.val
                    else:
                        res = min(res, q.val)
                if q.left:
                    tmp_list.append(q.left)
                    tmp_list.append(q.right)
            return bfs(tmp_list)
        bfs([root])
        return res
