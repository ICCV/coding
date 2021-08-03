class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        status = [[0]*n for i in range(n)]
        res = s[0]
        max_cnt = 1
        for j in range(1,n):
            for i in range(j):
                print(i,j)
                if s[i]==s[j] and (status[i+1][j-1] or j-i<=2):
                    status[i][j] = 1
                    if j-i+1>max_cnt:
                        max_cnt = j-i+1
                        res = ''.join(s[i:j+1])
        return res

if __name__ == '__main__':
    s = Solution()
    str1 = 'aaaa'
    print(s.longestPalindrome(str1))