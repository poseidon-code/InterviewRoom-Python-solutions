# PROBLEM: Coin change
# https://leetcode.com/problems/coin-change/


from typing import List

# SOLUTION
def change (coins: List[int], amount: int) -> int:
    need = [amount+1] * (amount+1)
    need[0] = 0

    for c in coins:
        for a in range(c, amount+1):
            need[a] = min(need[a], need[a-c]+1)
    
    return -1 if need[-1] > amount else need[-1]



if __name__ == "__main__":
    # INPUT :
    nums = [1,2,5]
    amount = 11

    # OUTPUT :
    print(change(nums, amount))