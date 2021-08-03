class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1),len(word2)
        status = [[-1]*(n+1)for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    status[i][j] = max(i, j)
                else:
                    if word1[i-1] == word2[j-1]:
                        status[i][j] = status[i-1][j-1]
                    else:
                        status[i][j] = min(status[i-1][j-1]+1,status[i-1][j]+1,status[i][j-1]+1)
        return status[m][n]


if __name__ == '__main__':
    s = Solution()
    word1 = 'horse'
    word2 = 'ros'
    print(s.minDistance(word1,word2))