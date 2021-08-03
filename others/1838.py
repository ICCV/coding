class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        max_frequency = 1
        i,n=0,len(nums)
        use_k = 0
        for j in range(1,n):
            use_k += (j-i)*(nums[j]-nums[j-1])
            while(use_k>k):
                use_k = use_k - (nums[j]-nums[i])
                i = i+1
            max_frequency = max(j-i+1,max_frequency)
        return max_frequency

if __name__ == '__main__':
    nums = [9930, 9923, 9983, 9997, 9934, 9952, 9945, 9914, 9985, 9982, 9970, 9932, 9985, 9902, 9975, 9990, 9922, 9990, 9994,
     9937, 9996, 9964, 9943, 9963, 9911, 9925, 9935, 9945, 9933, 9916, 9930, 9938, 10000, 9916, 9911, 9959, 9957, 9907,
     9913, 9916, 9993, 9930, 9975, 9924, 9988, 9923, 9910, 9925, 9977, 9981, 9927, 9930, 9927, 9925, 9923, 9904, 9928,
     9928, 9986, 9903, 9985, 9954, 9938, 9911, 9952, 9974, 9926, 9920, 9972, 9983, 9973, 9917, 9995, 9973, 9977, 9947,
     9936, 9975, 9954, 9932, 9964, 9972, 9935, 9946, 9966]
    k = 3056
    s = Solution()
    print(s.maxFrequency(nums,k))