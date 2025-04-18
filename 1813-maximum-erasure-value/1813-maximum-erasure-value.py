class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        msum = 0
        csum = 0
        s = set()

        for r in range(len(nums)):
            while nums[r] in s:
                s.remove(nums[l])
                csum -= nums[l]
                l += 1
            
            s.add(nums[r])
            csum += nums[r]
            msum = max(msum,csum)

        return msum