class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp_max = [float('-inf')]*n
        dp_min = [float('inf')]*n
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1,n):
            if nums[i]==0:
                dp_max[i] = 0
                dp_min[i] = 0
            elif nums[i]>0:
                if dp_max[i-1]>0:
                    dp_max[i] = dp_max[i-1]*nums[i]
                else:
                    dp_max[i] = nums[i]
                if dp_min[i-1]>0:
                    dp_min[i] = nums[i]
                else:
                    dp_min[i] = dp_min[i-1]*nums[i]
            else:
                if dp_min[i-1]<=0:
                    dp_max[i] = dp_min[i-1]*nums[i]
                else:
                    dp_max[i] = nums[i]
                if dp_max[i-1]<=0:
                    dp_min[i] = nums[i]
                else:
                    dp_min[i] = dp_max[i-1]*nums[i]

        return max(dp_max)

if __name__ == '__main__':
    ob = Solution()
    nums = [2,3,-2,4]
    print(ob.maxProduct(nums))