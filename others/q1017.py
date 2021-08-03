class Solution:
    def baseNeg2(self, N: int) -> str:
        res=""
        while N:
            N,mod=-(N>>1),N%2
            print(N,mod)
            res=str(mod)+res
        return res if res else "0"

if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.baseNeg2(n))