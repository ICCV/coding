class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        res = []
        while label>=1:
            res.append(label)
            label = int(label/2)
        res.reverse()
        for i,v in enumerate(res[:-1]):
            if (i+1)%2==1-len(res)%2:
                res[i] = pow(2,i)+pow(2,i+1)-1-v
        return res

if __name__ == '__main__':
    s = Solution()
    label = 26
    print(s.pathInZigZagTree(label))