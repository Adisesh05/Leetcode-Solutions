class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        sums = list(accumulate(nums, initial=0)) # get prefix sums
        return max(sums) - min(sums)