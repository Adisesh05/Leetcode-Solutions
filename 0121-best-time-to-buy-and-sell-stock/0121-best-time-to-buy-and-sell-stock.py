class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        pro = 0

        for r in range(len(prices)):
            if prices[L] > prices[r]:
                L = r
            pro = max(pro,abs(prices[r] - prices[L]))
        return pro