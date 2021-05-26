class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 1
        start = 0
        end = 1

        if n < 2:
            return n

        while start < n - 1:
            x = s[start: end]
            while end < n and s[end] not in x:
                x = x + s[end]
                max_len = max(max_len, len(x))
                end += 1
            start += 1
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
