class Solution:
  def longestMonotonicSubarray(self, nums: list[int]) -> int:
    res = 1
    inc = 1
    dec = 1
    for i in range(1, len(nums)):
      if nums[i] > nums[i - 1]:
        inc += 1
        dec = 1
      elif nums[i] < nums[i - 1]:
        dec += 1
        inc = 1
      else:
        inc = 1
        dec = 1
      res = max(res, inc, dec)
    return res