class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sorted_nums1 = sorted(nums1)
        res = 0
        mx = 0
        for num1,num2 in zip(nums1, nums2):
            gap = abs(num1-num2)
            res += gap
            left,right = 0,len(nums1)-1
            while left < right:
                mid = int((left+right)/2)
                if sorted_nums1[mid]<num2:
                    left = mid+1
                else:
                    right = mid
            mx = max(mx,gap - (min(abs(sorted_nums1[left-1]-num2),abs(sorted_nums1[left]-num2)) if left-1>=0 else abs(sorted_nums1[left]-num2)))
        return (res - mx) % (pow(10,9)+7)

if __name__ == '__main__':
    nums1 = [1,10,4,4,2,7]
    nums2 = [9,3,5,1,7,4]
    s = Solution()
    print(s.minAbsoluteSumDiff(nums1,nums2))