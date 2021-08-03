"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res =[]
        path = []
        size = len(candidates)
        def dfs(begin,target,path):
            if target == 0:
                res.append(path)
                return
            if target < 0:
                return
            for j in range(begin,size):
                if candidates[j] > target:
                    break
                dfs(j,target-candidates[j],path+[candidates[j]])
        dfs(0,target,path)
        return res

if __name__ == '__main__':
    s = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(s.combinationSum(candidates,target))