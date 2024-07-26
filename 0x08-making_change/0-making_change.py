#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0
    # Initialize the DP array with a large value (infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins to make amount 0
    # Iterate over each amount from 1 to total
    for amount in range(1, total + 1):
        # Check each coin
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    # If dp[total] is still infinity, it means we can't form the amount
    return dp[total] if dp[total] != float('inf') else -1
