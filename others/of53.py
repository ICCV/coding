class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i,j = 0,len(nums)-1
        while i < j:
            mid = int((i+j)/2)
            v = nums[mid]
            if v>= target:
                j = mid
            else:
                i = mid+1
        cnt = 0
        for k in range(i,len(nums)):
            if nums[k] == target:
                cnt += 1
        return cnt

if __name__ == '__main__':
    s = Solution()
    nums = [1]
    target = 1
    print(s.search(nums,target))