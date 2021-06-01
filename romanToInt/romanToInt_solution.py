class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = roman_to_int_map[s[-1]]
        for i in range(len(s) - 1):
            if roman_to_int_map[s[i]] < roman_to_int_map[s[i + 1]]:
                result -= roman_to_int_map[s[i]]
            else:
                result += roman_to_int_map[s[i]]
        return result


if __name__ == '__main__':
    S = Solution()
    assert S.romanToInt("III") == 3, "III"
    assert S.romanToInt("IV") == 4, "IV"
    assert S.romanToInt("IX") == 9, "IX"
    assert S.romanToInt("LVIII") == 58, "LVIII"
    assert S.romanToInt("MCMXCIV") == 1994, "MCMXCIV"
    assert S.romanToInt("MMDLIV") == 2554, "MMDLIV"
