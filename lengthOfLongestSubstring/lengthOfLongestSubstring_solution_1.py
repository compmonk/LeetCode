class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        Optimized Sliding Window technique
        """
        n = len(s)
        max_len = 0
        left = 0
        right = 0
        char_map = {}

        while right < n:
            if s[right] in char_map:
                left = max(char_map[s[right]], left)
            max_len = max(max_len, right - left + 1)
            char_map[s[right]] = right + 1
            right += 1

        return max_len


if __name__ == '__main__':
    S = Solution()
    assert S.lengthOfLongestSubstring("abcabcbb") == 3, "abcabcbb => abc"
    assert S.lengthOfLongestSubstring("bbbbb") == 1, "bbbbb => b"
    assert S.lengthOfLongestSubstring("pwwkew") == 3, "pwwkew => wke"
    assert S.lengthOfLongestSubstring("") == 0, ""
    assert S.lengthOfLongestSubstring(" ") == 1, " "
    assert S.lengthOfLongestSubstring("au") == 2, "au"
    assert S.lengthOfLongestSubstring("aa") == 1, "a"
