#-*- coding:utf-8 -*-
'''
有台奇怪的打印机有以下两个特殊要求：

打印机每次只能打印由 同一个字符 组成的序列。
每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。
'''

'''
f(i,j) 表示打印i到j之间(包括i,j)字符串的最少打印次数
1.若s[i]==s[j],则f(i,j) = f(i,j-1);如何理解，打印s[i]的时候，顺便把s[j]也打印；
2.若s[i]!=s[j],
注意到 f[i][j]f[i][j] 的计算需要用到 f[i][k]f[i][k] 和 f[k+1][j]f[k+1][j]（其中 i\leq k< ji≤k<j）。
为了保证动态规划的计算过程满足无后效性，在实际代码中，我们需要改变动态规划的计算顺序，
从大到小地枚举 ii，并从小到大地枚举 jj，这样可以保证当计算 f[i][j]f[i][j] 时，f[i][k]f[i][k] 和 f[k+1][j]f[k+1][j] 都已经被计算过。
'''

class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        dps = [[0] * len(s) for i in range(len(s))]
        def minPrint(i,j):
            # print(i,j)
            if i==j:
                dps[i][j] = 1
                return 1
            if s[i] == s[j]:
                if dps[i][j-1]:
                    dps[i][j] = dps[i][j-1]
                    return dps[i][j-1]
                else:
                    return minPrint(i,j-1)
            else:
                init_count = 10000
                for k in range(i,j):
                    min_count = (dps[i][k] if dps[i][k] else minPrint(i,k))  + (dps[k+1][j] if dps[k+1][j] else minPrint(k+1,j))
                    if min_count<init_count:
                        init_count = min_count
                dps[i][j] = init_count
                return init_count
        return minPrint(0,len(s)-1)



if __name__ == '__main__':
    ob = Solution()
    s = "baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa"
    print(ob.strangePrinter(s))
