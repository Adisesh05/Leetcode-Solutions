class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d={}
        m=-1
        for i in range(len(nums)):
            sd=0
            for j in str(nums[i]):
                sd+=int(j)
            if sd not in d:
                d[sd]=nums[i]
            else:
                m=max(d[sd]+nums[i],m)
                d[sd]=max(d[sd],nums[i])
        return m