# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def bfs(node_list,d,res):
            if not node_list:
                return res

            tmp_list = []
            #判断node_list是否满足要求
            is_odd = True
            last_node_val = node_list[0].val
            for i,node in enumerate(node_list):
                if d%2==0:
                    if (i!=0 and node.val<=last_node_val) or node.val%2==0:
                        is_odd = False
                        break
                else:
                    if (i != 0 and node.val >= last_node_val) or node.val%2==1:
                        is_odd = False
                        break
                last_node_val = node.val
                if node.left:
                    tmp_list.append(node.left)
                if node.right:
                    tmp_list.append(node.right)
            if is_odd:
                return bfs(tmp_list,d+1,res)
            else:
                return False
        return bfs([root],0,True)