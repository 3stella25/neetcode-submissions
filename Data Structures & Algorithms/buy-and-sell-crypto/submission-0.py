class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #return max profit, else 0
        max_profit = 0
        left = 0
        for right in range(len(prices)):
            running_profit = prices[right] - prices[left]
            max_profit = max(max_profit, running_profit)
            if prices[left] > prices[right]:
                left = right #Move buy to sell to maximize profit
        return max_profit

        