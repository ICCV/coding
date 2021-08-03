class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_num = sorted(nums)
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] != sort_num[i]:
                start = i
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j] != sort_num[j]:
                end = j
                break
        if start==-1 or end ==-1:
            return 0
        else:
            return end-start+1


if __name__ == '__main__':
    s = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(s.findUnsortedSubarray(nums))