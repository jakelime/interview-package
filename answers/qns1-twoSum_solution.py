class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for a in range(n):
            for b in range(a + 1, n):
                check = nums[a] + nums[b]
                if check == target:
                    return [a, b]
