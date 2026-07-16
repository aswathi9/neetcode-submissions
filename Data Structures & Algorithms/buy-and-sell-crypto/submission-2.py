class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice=prices[0]
        profit=0
        maxprofit=0
        for price in prices:
            buyprice=min(price,buyprice)
            profit=price-buyprice
            maxprofit=max(profit,maxprofit)
        return maxprofit