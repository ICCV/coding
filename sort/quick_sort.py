class Solution(object):
    def sort1(self, nums):
        """
        :type nums: list
        :rtype: list
        """
        def get_index(nums,left,right):
            temp = nums[left]
            while left<right:
                while left<right and nums[right]>=temp:
                    right = right-1
                nums[left] = nums[right]
                while left<right and nums[left]<=temp:
                    left = left+1
                nums[right] = nums[left]
            nums[left] = temp
            return left

        def quick_sort(nums,left,right):
            if (left<right):
                index = get_index(nums,left,right)
                quick_sort(nums,left,index-1)
                quick_sort(nums,index+1,right)
        quick_sort(nums,0,len(nums)-1)
        return nums
    def sort2(self,nums):
        
        def merge_sort(nums,)

if __name__ == '__main__':
    s = Solution()
    nums = [2,8,5,7,2,9,4,5,1,9]
    print(s.sor1(nums))