"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        path = []
        size = len(candidates)
        def dfs(begin,target,path):
            if target == 0:
                res.append(path)
                return
            for j in range(begin,size):
                if candidates[j] > target:
                    break
                if j>begin and candidates[j] == candidates[j-1]:
                    continue
                dfs(j+1,target-candidates[j],path+[candidates[j]])
        dfs(0,target,path)
        return res

if __name__ == '__main__':
    s = Solution()
    candidates = [2,5,2,1,2]
    target = 5
    print(s.combinationSum2(candidates,target))