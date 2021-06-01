class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        int_to_roman_map = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        result = ""
        tens_power = 0
        while num > 0:
            num, remainder = divmod(num, 10)
            if remainder <= 3:
                result = int_to_roman_map[1 * pow(10, tens_power)] * remainder + result
            elif remainder <= 5:
                result = int_to_roman_map[1 * pow(10, tens_power)] * (5 - remainder) + int_to_roman_map[
                    5 * pow(10, tens_power)] + result
            elif remainder <= 8:
                result = int_to_roman_map[5 * pow(10, tens_power)] + int_to_roman_map[1 * pow(10, tens_power)] * (
                            remainder - 5) + result
            elif remainder <= 10:
                result = int_to_roman_map[1 * pow(10, tens_power)] * (10 - remainder) + int_to_roman_map[
                    10 * pow(10, tens_power)] + result
            tens_power += 1
        return result


if __name__ == '__main__':
    S = Solution()
    assert S.intToRoman(3) == "III", 3
    assert S.intToRoman(4) == "IV", 4
    assert S.intToRoman(9) == "IX", 9
    assert S.intToRoman(58) == "LVIII", 58
    assert S.intToRoman(1994) == "MCMXCIV", 1994
    assert S.intToRoman(2554) == "MMDLIV", 2554
