class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums2) % 2 == 1:
            for i in nums1:
                res ^= i
        if len(nums1) % 2 == 1:
            for j in nums2:
                res ^= j
        return res