from collections import defaultdict
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        pre_dict = defaultdict(int)
        sum_count = 0
        res = 0
        for num in nums:
            pre_dict[sum_count] += 1
            sum_count += num
            res += pre_dict[sum_count-goal]

        return res





if __name__ == '__main__':
    nums = [0,0,0,0,0]
    goal = 0
    s = Solution()
    print(s.numSubarraysWithSum(nums,goal))