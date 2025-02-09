class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}
        pairs = 0

        for i, num in enumerate(nums):
            key = num - i
            pairs += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        n = len(nums)
        return (n * (n - 1)) // 2 - pairs