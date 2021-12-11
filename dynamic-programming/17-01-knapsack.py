# PROBLEM: 01 Knapsack
# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0

from typing import List

# SOLUTION
def knapsack (W: int, weights: List[int], values: List[int], N: int) -> int:
    dp =[0]*(W+1)

    for i in range(1, N+1):
        for w in range(W, -1, -1):
            if weights[i-1] <= w:
                dp[w] = max(dp[w], dp[w - weights[i-1]] + values[i-1])
    
    return dp[W]


if __name__ == "__main__":
    # INPUT :
    N = 3
    W = 4
    values = [1,2,3]
    weights = [4,5,1]

    # OUTPUT :
    print(knapsack(W, weights, values, N))