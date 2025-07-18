class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        a=0
        p=prices[0]
        for i in range(1,len(prices)):
            p=min(p,prices[i])
            a=max(a,prices[i]-p)
        return a

        