# PROBLEM: Coin sum infinite
# https://www.interviewbit.com/problems/coin-sum-infinite/


from typing import List

# SOLUTION
def coin_sum (s: List[int], n: int) -> int: 
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(len(s)):
        j=s[i]
        while j<=n:
            dp[j] += dp[j-s[i]]
            j+=1
    
    return dp[n]


if __name__ == "__main__":
    # INPUT :
    s = [1,2,3]
    n = 4

    # OUTPUT :
    print(coin_sum(s, n))