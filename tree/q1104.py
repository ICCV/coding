class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        res = []
        def dfs(d):
            if len(res)>0 and res[-1] == label:
                return
            if d%2 == 1:
                start, end = pow(2,d-1), pow(2,d)-1
            else:
                start, end = pow(2,d)-1, pow(2,d-1)
            for ele in range(start,end+1):
                if ele>label:
                    return
                else:
                    res.append(ele)
                    if ele == label:
                        return
                    else:
                        dfs(d+1)

