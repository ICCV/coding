"""
当 n>2n>2 时，如何计算 f(n)f(n) 的值？考虑第 11 位乘客选择的座位，有以下三种情况。

第 11 位乘客有 \frac{1}{n}
n
1
​
  的概率选择第 11 个座位，则所有乘客都可以坐在自己的座位上，此时第 nn 位乘客坐在自己的座位上的概率是 1.01.0。

第 11 位乘客有 \frac{1}{n}
n
1
​
  的概率选择第 nn 个座位，则第 22 位乘客到第 n-1n−1 位乘客都可以坐在自己的座位上，第 nn 位乘客只能坐在第 11 个座位上，此时第 nn 位乘客坐在自己的座位上的概率是 0.00.0。

第 11 位乘客有 \frac{n-2}{n}
n
n−2
​
  的概率选择其余的座位，每个座位被选中的概率是 \frac{1}{n}
n
1
​
 。
假设第 11 位乘客选择第 ii 个座位，其中 2 \le i \le n-12≤i≤n−1，则第 22 位乘客到第 i-1i−1 位乘客都可以坐在自己的座位上，第 ii 位乘客到第 nn 位乘客的座位不确定，第 ii 位乘客会在剩下的 n-(i-1)=n-i+1n−(i−1)=n−i+1 个座位中随机选择（包括第 11 个座位和第 i+1i+1 个座位到第 nn 个座位）。由于此时剩下的乘客数和座位数都是 n-i+1n−i+1，有 11 位乘客会随机选择座位，因此问题规模从 nn 减小至 n-i+1n−i+1。


"""


class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 0.5
        status = [0] * (n+1)
        status[2] = 0.5
        for i in range(3,n+1):
            r = 1.0*status[i-1]/(i-1)
            dp[i] = r
            status[i] = status[i-1]*(1-r)
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print(s.nthPersonGetsNthSeat(3))