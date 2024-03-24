class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy_price = float('inf')
        max_profit = 0
        for i in range(0,n):
            if buy_price > prices[i]:
                buy_price = prices[i]
            elif prices[i]- buy_price > max_profit:
                max_profit = prices[i] - buy_price
        
        return max_profit if max_profit > 0 else 0
        

        