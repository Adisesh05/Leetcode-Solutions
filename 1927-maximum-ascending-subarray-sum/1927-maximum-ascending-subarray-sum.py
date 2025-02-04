class Solution:
  def maxAscendingSum(self, nums: list[int]) -> int:
    res = 0
    sum1 = nums[0]
    for i in range(1, len(nums)):
      if nums[i] > nums[i - 1]:
        sum1 += nums[i]
      else:
        res = max(res, sum1)
        sum1 = nums[i]
    return max(res, sum1)