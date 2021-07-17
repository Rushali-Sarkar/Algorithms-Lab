def knapsack(weights: [int], values: [int], maximum_weight: int) -> int:

    dp_table = [0 for i in range(maximum_weight + 1)]

    for i in range(1, len(weights) + 1):
        for j in range(maximum_weight, 0, -1):
            if weights[i - 1] <= maximum_weight:
                dp_table[j] = max(dp_table[j], dp_table[j - weights[i - 1]] + values[i - 1])

    return dp_table[maximum_weight]



if __name__ == "__main__":

    print("Enter the weights")
    weights = list(map(int, input().split()))
    print("Enter the values")
    values = list(map(int, input().split()))
    print("Enter the maximum weight")
    maximum_weight = int(input())
    print("The best possible answer is: ")
    print(knapsack(weights, values, maximum_weight))
            
