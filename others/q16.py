class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dis = abs(nums[0]+nums[1]+nums[2]-target)
        res = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                if abs(nums[i]+nums[j]+nums[k]-target)<dis:
                    res = nums[i]+nums[j]+nums[k]
                    dis = abs(nums[i]+nums[j]+nums[k]-target)
                if nums[i]+nums[j]+nums[k]>target:
                    k = k - 1
                elif nums[i]+nums[j]+nums[k]<target:
                    j = j + 1
                else:
                    return res
        return res