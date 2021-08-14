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

        def merge(a,b):
            c = []
            i,j=0,0
            while i<=len(a) and j<=len(b):
                if i==len(a):
                    c = c + b[j:]
                    break
                if j==len(b):
                    c = c + a[i:]
                    break
                if a[i]<b[j]:
                    c.append(a[i])
                    i = i+1
                else:
                    c.append(b[j])
                    j = j+1
            return c

        def merge_sort(nums):
            if len(nums)<=1:
                return nums
            m = int(len(nums)/2)
            a = merge_sort(nums[:m])
            b = merge_sort(nums[m:])
            return merge(a,b)
        return merge_sort(nums)

if __name__ == '__main__':
    s = Solution()
    nums = [2,8,5,7,2,9,4,5,1,9]
    print(s.sort2(nums))