class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        max_Profit=0

        while right<len(prices):
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                max_Profit=max(max_Profit,profit)
            
            else:
                left=right
            right+=1
        
        return max_Profit