class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos_dict = {}
        left = 0
        max_substring=0
        for right in range(len(s)):
            if s[right] in pos_dict:
                left = max(pos_dict[s[right]]+1,left)
            pos_dict[s[right]] = right
            max_substring = max(max_substring,right-left+1)
        return max_substring

if __name__ == '__main__':
    s1 = Solution()
    s = 'abba'
    print(s1.lengthOfLongestSubstring(s))
