class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n = len(s),len(p)
        def matchers(i,j):
            if i == 0:
                return False
            if s[i-1] == '.':
                return True
            if s[i-1] == p[j-1]:
                return True
            else:
                return False
        status = [[False]*(n+1) for j in range(m+1)]
        status[0][0] = True
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1] == '*':
                    if matchers(i,j-1):
                        status[i][j] = (status[i-1][j] or status[i][j-2])
                    else:
                        status[i][j] = status[i][j-2]
                else:
                    if matchers(i, j):
                        status[i][j] = status[i - 1][j - 1]
        return status[m][n]

if __name__ == '__main__':
    s1 = Solution()
    s = 'aa'
    p = 'a*'
    print(s1.isMatch(s,p))