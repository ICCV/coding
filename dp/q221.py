import math


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        max_res = 0
        for i in range(m):
            if int(matrix[i][0]) == 1:
                max_res = 1
            dp[i][0] = int(matrix[i][0])
        for j in range(n):
            if int(matrix[0][j]) == 1:
                max_res = 1
            dp[0][j] = int(matrix[0][j])
        for i in range(1,m):
            for j in range(1,n):
                if dp[i-1][j-1]:
                    dis = int(math.sqrt(dp[i-1][j-1]))
                    min_gap = dis+1
                    for s in range(i,i-dis-1,-1):
                        if matrix[s][j] == '0':
                            min_gap = i-s
                            break
                    for s in range(j,j-dis-1,-1):
                        if matrix[i][s] == '0':
                            min_gap = min(min_gap,j-s)
                            break
                    dp[i][j] = min_gap*min_gap
                else:
                    dp[i][j] = max(0,int(matrix[i][j]))
                if dp[i][j]>max_res:
                    max_res = dp[i][j]
        return max_res

if __name__ == '__main__':
    ob = Solution()
    matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
    print(ob.maximalSquare(matrix))