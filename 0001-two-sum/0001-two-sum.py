class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i, n in enumerate(nums):
            c = target-n
            if c in a:
                return([a[c],i])
                break
            a[n]=i