class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        status = [0] * (n+1)
        status[0] = 1
        status[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                status[i] += status[j-1]*status[i-j]
        return status[n]

if __name__ == '__main__':
    s = Solution()
    n = 3
    s.numTrees(n)