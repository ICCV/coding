class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        hash_primes = set(primes)
        dp = [0]*n
        dp[0] = 1
        for i in range(1,n):
            j = dp[i-1] + 1
            while True:
                tmp_res = j
                s = len(primes)-1
                while s>=0:
                    if tmp_res in hash_primes or tmp_res==1:
                        tmp_res=1
                        break
                    if tmp_res% primes[s]==0:
                        tmp_res = tmp_res/primes[s]
                        s = s + 1
                    s = s - 1
                if tmp_res==1:
                    dp[i] = j
                    break
                else:
                    j = j + 1
        return dp[n-1]
if __name__ == '__main__':
    s1 = Solution()
    n = 12
    primes = [2,7,13,19]
    print(s1.nthSuperUglyNumber(n,primes))
