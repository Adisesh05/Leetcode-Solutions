class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k == 0:
            return 0
        
        left = 1
        right = max(candies)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if self.canDistribute(candies, k, mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return result
        
    def canDistribute(self, candies, k, x):
        count = 0
        for pile in candies:
            count += pile // x
            
        return count >= k   