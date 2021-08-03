# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        L1,L2 = headA,headB
        while L1!=L2:
            L1 = headB if L1==None else L1.next
            L2 = headA if L2== None else L2.next
        return L1