class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges.sort(key=lambda x:x[0])
        print(ranges)
        for r in ranges:
            if left< r[0]:
                return False
            else:
                left = max(r[1]+1,left)
            if left>right:
                return True
        return False



if __name__ == '__main__':
    s = Solution()
    ranges = [[13,43],[19,20],[32,38],[26,33],[3,38],[16,31],[26,48],[27,43],[12,24]]
    left = 36
    right = 45
    print(s.isCovered(ranges,left,right))
