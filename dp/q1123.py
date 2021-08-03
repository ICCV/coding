class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m,n = len(text1),len(text2)
        status = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    status[i][j] = status[i-1][j-1] +1
                else:
                    status[i][j] = max(status[i-1][j-1],status[i-1][j],status[i][j-1])
        return status[m][n]

if __name__ == '__main__':
    s = Solution()
    text1 = "abcde"
    text2 = "ace"
    print(s.longestCommonSubsequence(text1,text2))