# PROBLEM: Min cost climbing stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/


from typing import List

# SOLUTION
def min_cost (cost: List[int]) -> int: 
    for i in range(2, len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])

    return min(cost[len(cost)-1], cost[len(cost)-2])


if __name__ == "__main__":
    # INPUT :
    cost = [10,15,20]

    # OUTPUT :
    print(min_cost(cost))