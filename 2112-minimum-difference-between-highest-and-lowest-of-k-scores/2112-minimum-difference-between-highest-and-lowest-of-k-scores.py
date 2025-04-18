class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        if k == 1:
            return 0
        
        nums.sort()
        msum = float('inf')
        csum = 0
        for i in range(len(nums) - k + 1):
            csum = nums[i + k - 1] - nums[i]
            msum = min(msum,csum)
        return msum
