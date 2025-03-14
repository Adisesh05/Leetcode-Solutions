class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        pref = [0] * (len(nums)+1)
        s, k = 0, 0
        for i in range(len(nums)):
            diff = nums[i] - s
            while pref[i] < diff:  
                if k >= len(queries): 
                    return -1
                l, r, val = queries[k]
                if r >= i:
                    pref[max(l, i)] += val
                    pref[r+1] -= val
                k += 1
            s += pref[i]
        return k