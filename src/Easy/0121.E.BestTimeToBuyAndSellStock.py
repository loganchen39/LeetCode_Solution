# Algo. 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        : type prices: List[int]
        : rtype: int
        :
        : TC: O(n), 50.86%
        : SC: O(1), 5.03% (NOT correct!?)
        :\Algo. 1 as Approach 2 of One pass. The problem is simple, you only need to keep a 
        : previous min_price, which normally will be the buying price. 
        : An obvious BF algo. involves 2 for-loop to find the max_profit, as in A1.
        """
        n = len(prices)
        if n <= 1: return 0
        
        max_profit = 0
        min_price  = prices[0]
        for i in range(n):
            if prices[i] < min_price: min_price = prices[i]
            elif prices[i] - min_price > max_profit: max_profit = prices[i] - min_price

        return max_profit