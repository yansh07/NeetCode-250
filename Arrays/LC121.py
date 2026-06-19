# Best time to buy and sell stock

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf') # positive infinity value
        max_profit = 0 # max_profit initially will be zero
        
        for price in prices:
            # if price is less than infinity - will always be true
            if price < min_price:
                min_price = price
            #calc profit if sold today, and store the max value
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit