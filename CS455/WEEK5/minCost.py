from typing import List


def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


# Testing the function
prices = [7, 6, 4, 3, 1]
# Expected output: 5
print(f"MaxProfit: {maxProfit(prices)} with inputs: {prices}")