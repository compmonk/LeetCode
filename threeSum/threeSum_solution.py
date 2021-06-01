class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        hash_map = {x: i for i, x in enumerate(nums)}
        result = set()

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                z = -(nums[i] + nums[j])
                index = hash_map.get(z, None)
                if index and i < j < index:
                    result.add(tuple(sorted((nums[i], nums[j], z))))
        return [list(_) for _ in result]


if __name__ == '__main__':
    S = Solution()
    assert S.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]], [-1, 0, 1, 2, -1, -4]
    assert S.threeSum([]) == [], []
    assert S.threeSum([0]) == [], [0]
