class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap = prices[0]
        res = float("-inf")
        for price in prices:
            res =max(res, price -cheap)
            if price < cheap:
                cheap = price
        return res
            