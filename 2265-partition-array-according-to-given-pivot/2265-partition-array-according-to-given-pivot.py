class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        x1 = [x for x in nums if x<pivot]
        x2 = [x for x in nums if x>pivot]
        n = len(nums) - len(x1) - len(x2)
        x3 = [pivot]*n
        return x1+x3+x2