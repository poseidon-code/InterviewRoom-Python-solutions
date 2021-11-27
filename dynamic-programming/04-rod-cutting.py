# PROBLEM: Rod cutting
# https://www.geeksforgeeks.org/cutting-a-rod-dp-13/


from typing import List

# SOLUTION
INT_MIN = -2**16
def cutting (price: List[int], n: int) -> int: 
    result = [0]*(n+1)
    result[0] = 0

    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, price[j] + result[i-j-1])
        result[i] = max_val
    
    return result[n]



if __name__ == "__main__":
    # INPUT :
    price = [1,5,8,9,10,17,17,20]
    n = 8

    # OUTPUT :
    print(cutting(price, n))