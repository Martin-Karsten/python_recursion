class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:            
        memo = {}

        def dfs(coins, amount):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')

            # check for every coin, how many coins it takes to reach 0 or less
            # everytime we call dfs() amount is reduced by the current coin
            # for every reduced amount we check for every coin again how many coins it takes to reach 0 or less
            # to reduce repeition we use memo
            # eg [1,2,3] 4
            # dfs so many times until we reach the base case -> amount == 0 or less
              # check how many coins it takes for 1,2,3 to reach 0 or less   
              # check how many coins it takes for 1,2,3 to reach 1 or less  -> # how many coins it takes for 1,2,3 to reach 0 or less
              # check how many coins it takes for 1,2,3 to reach 2 or less  -> how many coins it takes for 1,2,3 to reach 1 or less   -> how many coins it takes for 1,2,3 to reach 0 or less
              # check how many coins it takes for 1,2,3 to reach 3 or less  -> for 1,2,3 to reach 2 or less   -> for 1,2,3 to reach 1 or less -> for 1,2,3 to reach 0 or less
              # check how many coins it takes for 1,2,3 to reach 4 or less  -> for 1,2,3 to reach 3 or less   -> for 1,2,3 to reach 2 or less -> for 1,2,3 to reach 1 or less -> for 1,2,3 to reach 0 or less
            # evyertime we end a dfs() cycle we add + 1 because it represents the current coin. 1 + dfs() -> 1 + everything that came before
            # for steps we already visited we use memo
            # in every dfs call minCoins is reset to float('inf')
                # that way on every for loop (in a dfs() cyble) we can decide which coin combination was of [1,2,3] took the least to reach the amount in the current dfs() cycle
            minCoins = float('inf')
            for coin in coins:
                numCoins = 1 +dfs(coins, amount - coin)
                minCoins = min(minCoins, numCoins)
            memo[amount]= minCoins

            return minCoins
        
        res = dfs(coins, amount)
        if res == float('inf'):
            return -1
        else:
            return res 