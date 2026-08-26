class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currbest = prices[0]
        currMax = 0
        for num in prices:
            currbest = min(num, currbest)
            if num - currbest > currMax:
                currMax = num - currbest
        return currMax
            
            
            