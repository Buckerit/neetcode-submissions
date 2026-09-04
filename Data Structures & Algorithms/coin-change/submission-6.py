class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        reverseCoins = sorted(coins, reverse=True)
        if amount == 0:
            return 0
        hashmap = {}
        visited = set()

        def dp(revCoins, amount):
            needed = -1
            if amount == 0:
                return 0
            for coin in revCoins:
                newAmount = amount - coin
                if newAmount < 0:
                    continue
                elif newAmount == 0:
                    return 1
                else:    
                    if newAmount not in visited:
                        numCoins = dp(coins, newAmount) 
                    else:
                        numCoins = hashmap[newAmount]                    
                if numCoins != -1:
                    if numCoins+1 < needed or needed < 0:
                        needed = numCoins + 1
            hashmap[amount] = needed
            visited.add(amount)
            return needed
         
        answer = dp(reverseCoins,amount)
        return answer
            
        