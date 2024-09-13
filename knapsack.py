def fractional_knapsack(capacity, weights, profit):
    """
    Solves the fractional knapsack problem using a greedy approach.

    Args:
        capacity (int): The maximum capacity of the knapsack.
        weights (list): A list of item weights.
        profit (list): A list of item profit.

    Returns:
        float: The maximum total value that can be achieved.
    """

    n = len(weights)
    print(n)  # it will print value of n
    items = []

    # Calculate value-to-weight ratios for each item
    for i in range(n):
        print("value of i ",i)
        # ratio = profit[i] / weights[i]
        ratio = round(profit[i] / weights[i], 2)
        items.append((ratio, weights[i], profit[i]))
        print("value of items ",items)

    # Sort items by their value-to-weight ratio in descending order
    items.sort(reverse=True)
    print("print sorted value of items ",items)
    total_value = 0
    remaining_capacity = capacity

    for ratio, weight, value in items:
        if weight <= remaining_capacity:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take a fraction of the item
            fraction = remaining_capacity / weight
            total_value += fraction * value
            break  # Knapsack is full

    return total_value

# Example usage
capacity = 12
weights = [2,5,3,4,6]
profit = [15,12,9,16,17]

max_value = fractional_knapsack(capacity, weights, profit)
print("Maximum value:", max_value)