class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currbest = prices[0]
        currMax = 0
        for num in prices:
            currbest = min(num, currbest)
            currMax = max(currMax, num - currbest)
        return currMax


            
            