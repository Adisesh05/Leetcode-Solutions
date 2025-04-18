class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        pro = 0

        for r in range(len(prices)):
            while prices[L] > prices[r]:
                L += 1
            pro = max(pro,abs(prices[r] - prices[L]))
        return pro