class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        mlen = float('inf')
        csum = 0

        for r in range(len(nums)):
            csum += nums[r]
            while csum >= target:
                mlen = min(mlen,r-l+1)
                csum -= nums[l]
                l += 1

        return 0 if mlen == float('inf') else mlen

