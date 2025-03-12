class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l = len(nums)
        zero = 0
        c = 0
        for i in range(l):
            if nums[i] < 0:
                c += 1
            elif nums[i] == 0:
                zero += 1
        return max(l-c-zero,c)