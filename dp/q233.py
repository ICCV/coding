class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = [0] * n
        for i in range(0,n):
            num = i+1
            count1= 0
            for nu in str(num):
                if nu=='1':
                    count1 += 1
            dp[i] = dp[i-1] + count1
        return dp[n-1]



if __name__ == '__main__':
    ob = Solution()
    n = 13
    print(ob.countDigitOne(n))