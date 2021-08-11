class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        set1 = set()
        for edge in edges:
            if edge[1] not in set1:
                set1.add(edge[1])
        res = []
        for i in range(n):
            if i not in set1:
                res.append(i)
        return list(set(res))