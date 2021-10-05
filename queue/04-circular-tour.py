# PROBLEM: Circular tour
# https://leetcode.com/problems/gas-station/
# https://practice.geeksforgeeks.org/problems/circular-tour/1


from typing import List

# SOLUTION
def circular_tour (gas: List[int], cost: List[int]) -> int:
    start = total = tank = 0

    for i in range(len(gas)):
        tank += gas[i]-cost[i]
        if tank < 0:
            start = i+1
            total += tank
            tank = 0
    
    return (-1 if (total+tank<0) else start)



if __name__ == "__main__":
    # INPUT :
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    # OUTPUT :
    print(circular_tour(gas, cost))