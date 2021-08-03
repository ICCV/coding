"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res= []
        path = []
        def dfs(begin,n,path):
            if n == 0 and len(path)==k:
                res.append(path)
                return
            for j in range(begin,9):
                if j+1>n or len(path)>k:
                    break
                dfs(j+1,n-(j+1),path+[j+1])
        dfs(0,n,path)
        return res

if __name__ == '__main__':
    s = Solution()
    k = 3
    n = 9
    print(s.combinationSum3(k,n))