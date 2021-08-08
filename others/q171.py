class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        for s in columnTitle:
            res *= 26
            res+=(ord(s) - ord('A')+1)
        return res

if __name__ == '__main__':
    s = Solution()
    columnTitle = 'AB'
    print(s.titleToNumber(columnTitle))