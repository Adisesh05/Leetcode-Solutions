class Solution:
    def check(self, nums: List[int]) -> bool:
        found = False
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                if found:
                    return False
                found = True
        return not found or nums[0] >= nums[n - 1]