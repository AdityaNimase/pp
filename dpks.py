def knapsack_dp(values, weights, capacity):
    n = len(values)
    #Create a 2D DP array with dimensions (n+1) x (capacity+1)
    dp = [[0] * (capacity+1) for _ in range(n+1)]

    #Build the DP table
    for i in range(1, n+1): #Iterate over each item
        print(f"\nConsidering item {i} (Value: {values[i-1]}, Weight: {weights[i-1]})")
        for w in range(1, capacity+1): #Iterate over each possible capacity
            if weights[i-1] <= w:
                #Option 1: Include the item
                include_value = values[i-1] + dp[i-1][w - weights[i-1]]
                exclude_value = dp[i-1][w]

                #Take the max of including or excluding it
                dp[i][w] = max(include_value, exclude_value)

                #Display details
                print(f"  Capacity {w}:")
                print(f"    -Option 1: Include item {i} -> New Value: {include_value} (Remaining capacity: {w - weights[i-1]})")
                print(f"    -Option 2: Exclude item {i} -> Value without it: {exclude_value}")
                print(f"    -Max value chosen: {dp[i][w]}")
            else:
                #Option 2: Cannot include this item, use the value from the row above
                dp[i][w] = dp[i-1][w]

                #Display details
                print(f"Capacity {w}: Item too heavy to include (weight {weights[i-1]}), taking value from above: {dp[i][w]}")

    #Display final DP table for reference
    print("\nDP Table:")
    for row in dp:
        print(row)

    #Result
    print(f"\nThe maximum value that can be placed in the knapsack is: {dp[n][capacity]}")
    return dp[n][capacity]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value = knapsack_dp(values, weights, capacity)
print(f"The maximum value that can be placed in the knapsack is: {max_value}")