class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mini = float(inf)
        cnt = 0
        uniq = set()
        for num in nums:
            if num < mini:
                mini = num
            if num not in uniq:
                uniq.add(num)
                cnt += 1
        if mini < k:
            return -1
        if mini == k:
            return cnt - 1
        else:
            return cnt
