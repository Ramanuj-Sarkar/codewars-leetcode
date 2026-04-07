# You have the values of coins in coins
# You have infinite coins of each value
# You have to make the amount of money using those coins, in the fewest number of coins.
# If the amount can't be made by any combination, return -1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # this is more than the amount could possibly be
        one_over = amount + 1

        # each index contains
        # the minimum number of coins required to get that index
        min_coins = [one_over] * one_over
        
        # 0 coins to get a value of 0
        min_coins[0] = 0

        for i in range(1, one_over):
            for c in coins:
                # makes sure the number is non-negative
                if i >= c:
                    # checks if 1 + the value w/o that coin is less than current
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])
        
        # if you can't get amount, then it will still be one_over
        # otherwise, it will be changed
        return min_coins[-1] if min_coins[-1] != one_over else -1
